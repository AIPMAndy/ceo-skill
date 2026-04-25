#!/usr/bin/env python3
"""
Bayesian Decision Calculator for CEO Skill

Provides tools for:
1. Prior to posterior updates using likelihood ratios
2. Beta-Binomial updates for trial data
3. Sensitivity analysis
4. Expected value calculations with probabilities
"""

import math
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass


@dataclass
class Evidence:
    """Single piece of evidence with quality grade and likelihood ratio"""
    description: str
    quality_grade: str  # A, B, C, D, E
    likelihood_ratio: float
    supports: bool  # True if supports hypothesis, False if contradicts


@dataclass
class BayesianUpdate:
    """Result of a Bayesian update"""
    prior_probability: float
    posterior_probability: float
    prior_odds: float
    posterior_odds: float
    evidence_count: int
    combined_lr: float
    confidence_change: str  # "Increased", "Decreased", "Stable"


def probability_to_odds(probability: float) -> float:
    """Convert probability to odds"""
    if probability <= 0 or probability >= 1:
        raise ValueError("Probability must be between 0 and 1 (exclusive)")
    return probability / (1 - probability)


def odds_to_probability(odds: float) -> float:
    """Convert odds to probability"""
    if odds < 0:
        raise ValueError("Odds must be non-negative")
    return odds / (1 + odds)


def update_belief(
    prior_probability: float,
    evidence_list: List[Evidence],
    dependency_discount: float = 1.0
) -> BayesianUpdate:
    """
    Update belief using multiple pieces of evidence
    
    Args:
        prior_probability: Initial belief (0-1)
        evidence_list: List of Evidence objects
        dependency_discount: Factor to account for evidence correlation (0-1)
                           1.0 = fully independent, <1.0 = some overlap
    
    Returns:
        BayesianUpdate object with results
    """
    if not 0 < prior_probability < 1:
        raise ValueError("Prior probability must be between 0 and 1")
    
    if not 0 < dependency_discount <= 1:
        raise ValueError("Dependency discount must be between 0 and 1")
    
    # Convert to odds
    prior_odds = probability_to_odds(prior_probability)
    
    # Multiply all likelihood ratios
    combined_lr = 1.0
    for evidence in evidence_list:
        # Apply dependency discount to reduce impact of correlated evidence
        adjusted_lr = 1 + (evidence.likelihood_ratio - 1) * dependency_discount
        combined_lr *= adjusted_lr
    
    # Calculate posterior odds
    posterior_odds = prior_odds * combined_lr
    
    # Convert back to probability
    posterior_probability = odds_to_probability(posterior_odds)
    
    # Determine confidence change
    if posterior_probability > prior_probability + 0.05:
        confidence_change = "Increased"
    elif posterior_probability < prior_probability - 0.05:
        confidence_change = "Decreased"
    else:
        confidence_change = "Stable"
    
    return BayesianUpdate(
        prior_probability=prior_probability,
        posterior_probability=posterior_probability,
        prior_odds=prior_odds,
        posterior_odds=posterior_odds,
        evidence_count=len(evidence_list),
        combined_lr=combined_lr,
        confidence_change=confidence_change
    )


def beta_binomial_update(
    prior_alpha: float,
    prior_beta: float,
    successes: int,
    trials: int
) -> Tuple[float, float, float]:
    """
    Update belief using Beta-Binomial conjugate prior
    
    Args:
        prior_alpha: Prior alpha parameter (pseudo-successes)
        prior_beta: Prior beta parameter (pseudo-failures)
        successes: Observed successes
        trials: Total trials
    
    Returns:
        (posterior_mean, posterior_alpha, posterior_beta)
    """
    if trials < 0 or successes < 0 or successes > trials:
        raise ValueError("Invalid trial data")
    
    failures = trials - successes
    
    # Update parameters
    posterior_alpha = prior_alpha + successes
    posterior_beta = prior_beta + failures
    
    # Calculate posterior mean
    posterior_mean = posterior_alpha / (posterior_alpha + posterior_beta)
    
    return posterior_mean, posterior_alpha, posterior_beta


def sensitivity_analysis(
    base_prior: float,
    evidence_list: List[Evidence],
    prior_range: float = 0.1,
    lr_multiplier_range: Tuple[float, float] = (0.5, 2.0)
) -> Dict[str, float]:
    """
    Test sensitivity of conclusion to assumption changes
    
    Args:
        base_prior: Base case prior probability
        evidence_list: List of evidence
        prior_range: +/- range to test for prior (default ±10%)
        lr_multiplier_range: (min, max) multipliers for LR (default 0.5x to 2x)
    
    Returns:
        Dictionary with best/base/worst case posteriors
    """
    # Base case
    base_result = update_belief(base_prior, evidence_list)
    
    # Best case: higher prior, stronger evidence
    best_prior = min(base_prior + prior_range, 0.99)
    best_evidence = [
        Evidence(
            e.description,
            e.quality_grade,
            e.likelihood_ratio * lr_multiplier_range[1],
            e.supports
        )
        for e in evidence_list
    ]
    best_result = update_belief(best_prior, best_evidence)
    
    # Worst case: lower prior, weaker evidence
    worst_prior = max(base_prior - prior_range, 0.01)
    worst_evidence = [
        Evidence(
            e.description,
            e.quality_grade,
            e.likelihood_ratio * lr_multiplier_range[0],
            e.supports
        )
        for e in evidence_list
    ]
    worst_result = update_belief(worst_prior, worst_evidence)
    
    return {
        "best_case": best_result.posterior_probability,
        "base_case": base_result.posterior_probability,
        "worst_case": worst_result.posterior_probability,
        "range": best_result.posterior_probability - worst_result.posterior_probability,
        "robust": (best_result.posterior_probability - worst_result.posterior_probability) < 0.2
    }


def expected_value(
    probability_success: float,
    value_if_success: float,
    cost_if_failure: float
) -> Dict[str, float]:
    """
    Calculate expected value of a decision
    
    Args:
        probability_success: P(success) from Bayesian update
        value_if_success: Payoff if hypothesis is true
        cost_if_failure: Cost if hypothesis is false
    
    Returns:
        Dictionary with EV and recommendation
    """
    probability_failure = 1 - probability_success
    
    ev = (probability_success * value_if_success) - (probability_failure * cost_if_failure)
    
    # Calculate break-even probability
    if value_if_success + cost_if_failure > 0:
        breakeven = cost_if_failure / (value_if_success + cost_if_failure)
    else:
        breakeven = None
    
    return {
        "expected_value": ev,
        "ev_success": probability_success * value_if_success,
        "ev_failure": probability_failure * cost_if_failure,
        "recommendation": "Go" if ev > 0 else "No-Go",
        "breakeven_probability": breakeven,
        "margin": probability_success - breakeven if breakeven else None
    }


def format_bayesian_report(
    hypothesis: str,
    prior_probability: float,
    prior_source: str,
    evidence_list: List[Evidence],
    value_if_success: Optional[float] = None,
    cost_if_failure: Optional[float] = None
) -> str:
    """
    Generate a formatted Bayesian decision report
    
    Args:
        hypothesis: Clear statement of what we're predicting
        prior_probability: Initial belief
        prior_source: Where the prior comes from
        evidence_list: List of Evidence objects
        value_if_success: Optional payoff for EV calculation
        cost_if_failure: Optional cost for EV calculation
    
    Returns:
        Formatted markdown report
    """
    # Perform update
    update = update_belief(prior_probability, evidence_list)
    
    # Sensitivity analysis
    sensitivity = sensitivity_analysis(prior_probability, evidence_list)
    
    # Expected value (if provided)
    ev_result = None
    if value_if_success is not None and cost_if_failure is not None:
        ev_result = expected_value(
            update.posterior_probability,
            value_if_success,
            cost_if_failure
        )
    
    # Build report
    report = f"""## Bayesian Decision Analysis: {hypothesis}

### Hypothesis
{hypothesis}

### Prior Belief
- **Probability:** {prior_probability:.1%}
- **Source:** {prior_source}
- **Prior Odds:** {update.prior_odds:.2f}:1

### Evidence Summary
"""
    
    for i, evidence in enumerate(evidence_list, 1):
        direction = "Supports" if evidence.supports else "Contradicts"
        report += f"{i}. **{evidence.description}**\n"
        report += f"   - Quality Grade: {evidence.quality_grade}\n"
        report += f"   - Likelihood Ratio: {evidence.likelihood_ratio:.2f}\n"
        report += f"   - Direction: {direction}\n\n"
    
    report += f"""### Updated Belief
- **Prior:** {update.prior_probability:.1%} → **Posterior:** {update.posterior_probability:.1%}
- **Posterior Odds:** {update.posterior_odds:.2f}:1
- **Combined LR:** {update.combined_lr:.2f}
- **Confidence Change:** {update.confidence_change}

### Sensitivity Analysis
- **Best Case:** {sensitivity['best_case']:.1%}
- **Base Case:** {sensitivity['base_case']:.1%}
- **Worst Case:** {sensitivity['worst_case']:.1%}
- **Range:** {sensitivity['range']:.1%}
- **Decision Robust?** {"Yes" if sensitivity['robust'] else "No - gather more evidence"}
"""
    
    if ev_result:
        report += f"""
### Expected Value Analysis
- **EV(Go):** ${ev_result['expected_value']:,.0f}
- **EV if Success:** ${ev_result['ev_success']:,.0f}
- **EV if Failure:** -${ev_result['ev_failure']:,.0f}
- **Break-even Probability:** {ev_result['breakeven_probability']:.1%}
- **Margin:** {ev_result['margin']:.1%}
- **Recommendation:** {ev_result['recommendation']}
"""
    
    return report


# Example usage
if __name__ == "__main__":
    # Example: Should we launch this new product?
    hypothesis = "Product will achieve 10,000 paying users within 12 months"
    
    # Prior: Industry benchmark for similar SaaS products
    prior = 0.30  # 30% base rate
    prior_source = "Industry benchmark: 30% of B2B SaaS products reach 10K users in year 1"
    
    # Evidence
    evidence = [
        Evidence(
            description="Beta test showed 40% daily active usage (vs 20% industry avg)",
            quality_grade="B",
            likelihood_ratio=5.0,
            supports=True
        ),
        Evidence(
            description="Similar competitor product failed to reach 5K users",
            quality_grade="C",
            likelihood_ratio=0.6,
            supports=False
        ),
        Evidence(
            description="Pre-launch waitlist has 2,000 signups",
            quality_grade="C",
            likelihood_ratio=3.0,
            supports=True
        )
    ]
    
    # Generate report
    report = format_bayesian_report(
        hypothesis=hypothesis,
        prior_probability=prior,
        prior_source=prior_source,
        evidence_list=evidence,
        value_if_success=5_000_000,  # $5M revenue potential
        cost_if_failure=500_000  # $500K development cost
    )
    
    print(report)
