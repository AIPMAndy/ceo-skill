# Bayesian Decision Analysis for CEOs

## When to Use This Framework

Use Bayesian analysis when:
- Making decisions under significant uncertainty
- You have some prior beliefs but new evidence is emerging
- You need to quantify confidence levels explicitly
- The decision involves probabilistic outcomes (market success, product adoption, competitive response)
- You want to update beliefs systematically as new data arrives

**Do NOT use for:**
- Decisions with complete information
- Pure ethical/values-based choices
- Situations requiring immediate action without time for analysis

---

## Core Concept

Bayesian thinking helps you:
1. Start with an initial belief (prior probability)
2. Gather evidence and assess its quality
3. Update your belief systematically (posterior probability)
4. Make decisions based on updated probabilities and expected values

**Key Formula:**
```
Posterior Odds = Prior Odds × Likelihood Ratio
```

Or in probability form:
```
P(H|E) = P(E|H) × P(H) / P(E)
```

Where:
- H = Hypothesis (e.g., "This product will succeed")
- E = Evidence (e.g., "Beta users showed 40% engagement")
- P(H|E) = Updated probability after seeing evidence

---

## Step-by-Step Process

### Step 1: Define the Hypothesis

Frame the decision as a clear hypothesis with:
- **Specific outcome**: What exactly are we predicting?
- **Time horizon**: By when?
- **Success metric**: How do we measure it?

**Example:**
- ❌ Bad: "Will this product work?"
- ✅ Good: "Will this product achieve 10,000 paying users within 12 months of launch?"

### Step 2: Set the Prior Probability

Establish your starting belief before seeing new evidence.

**Sources for priors (in order of strength):**

| Quality | Source | Example | Confidence |
|---------|--------|---------|------------|
| **Strong** | Industry benchmarks, historical data from similar initiatives | "SaaS products in this category have 15% success rate" | High |
| **Medium** | Expert judgment, analogous cases | "Our VP Product estimates 30% based on past launches" | Medium |
| **Weak** | Gut feeling, limited data | "I think there's a 50/50 chance" | Low |

**Prior Probability Range:**
- 0.01-0.10 (1-10%): Very unlikely
- 0.10-0.30 (10-30%): Unlikely but possible
- 0.30-0.70 (30-70%): Uncertain
- 0.70-0.90 (70-90%): Likely
- 0.90-0.99 (90-99%): Very likely

**Document:**
- Prior probability: [X%]
- Source: [Where this comes from]
- Confidence: [High/Medium/Low]
- Reference class: [What similar situations inform this?]

### Step 3: Grade Your Evidence

For each piece of evidence, assess quality:

| Grade | Source Type | Reliability | Use Case |
|-------|-------------|-------------|----------|
| **A** | Controlled experiments, regulatory data, peer-reviewed studies | Very High | Strong updates |
| **B** | Industry reports, validated surveys, public datasets | High | Medium updates |
| **C** | Expert opinions, internal data, customer interviews | Medium | Cautious updates |
| **D** | Analogies, heuristics, educated guesses | Low | Weak updates only |
| **E** | Anecdotes, social media, marketing claims | Very Low | Do not use |

**Evidence Quality Checklist:**
- [ ] Is the sample size adequate?
- [ ] Is the source independent and unbiased?
- [ ] Is the measurement method sound?
- [ ] Is the evidence recent and relevant?
- [ ] Are there confounding factors?

### Step 4: Calculate Likelihood Ratios

For each piece of evidence, determine how much it supports or contradicts your hypothesis.

**Likelihood Ratio (LR):**
```
LR = P(Evidence | Hypothesis True) / P(Evidence | Hypothesis False)
```

**Quick LR Guidelines:**

| Evidence Strength | LR Value | Interpretation |
|-------------------|----------|----------------|
| Strongly supports | 10-100 | Very strong evidence FOR |
| Moderately supports | 3-10 | Moderate evidence FOR |
| Weakly supports | 1.5-3 | Weak evidence FOR |
| Neutral | ~1 | No update |
| Weakly contradicts | 0.3-0.67 | Weak evidence AGAINST |
| Moderately contradicts | 0.1-0.3 | Moderate evidence AGAINST |
| Strongly contradicts | 0.01-0.1 | Very strong evidence AGAINST |

**Example:**
- Evidence: "Beta test showed 40% daily active usage"
- If hypothesis true (product succeeds): P(40% DAU | Success) = 0.70
- If hypothesis false (product fails): P(40% DAU | Failure) = 0.10
- LR = 0.70 / 0.10 = 7 (moderately supports)

### Step 5: Update Your Belief

**Method 1: Odds Form (Recommended for multiple evidence pieces)**

1. Convert prior probability to odds:
   ```
   Prior Odds = P(H) / (1 - P(H))
   ```

2. Multiply by each likelihood ratio:
   ```
   Posterior Odds = Prior Odds × LR₁ × LR₂ × LR₃ ...
   ```

3. Convert back to probability:
   ```
   Posterior Probability = Posterior Odds / (1 + Posterior Odds)
   ```

**Method 2: Direct Calculation (For single evidence)**

```
P(H|E) = [P(E|H) × P(H)] / [P(E|H) × P(H) + P(E|¬H) × P(¬H)]
```

**Example Calculation:**
- Prior: 30% chance of success
- Prior Odds: 0.30 / 0.70 = 0.43
- Evidence 1 (beta test): LR = 7
- Evidence 2 (competitor failed): LR = 0.5
- Posterior Odds: 0.43 × 7 × 0.5 = 1.5
- Posterior Probability: 1.5 / (1 + 1.5) = 60%

**Interpretation:** New evidence increased our confidence from 30% to 60%.

### Step 6: Sensitivity Analysis

Test how robust your conclusion is to changes in assumptions.

**Key Questions:**
1. What if the prior was 10% higher or lower?
2. What if the likelihood ratio was half or double?
3. What if we ignored the weakest evidence?
4. At what probability threshold would we change our decision?

**Sensitivity Test:**
```
Best Case: [Optimistic assumptions] → [X% probability]
Base Case: [Current assumptions] → [Y% probability]
Worst Case: [Pessimistic assumptions] → [Z% probability]
```

If the decision changes across scenarios, you need more evidence before committing.

### Step 7: Make the Decision

Combine updated probabilities with expected values:

```
Expected Value = (Probability of Success × Value if Success) - (Probability of Failure × Cost if Failure)
```

**Decision Rule:**
- If EV > 0 and posterior probability > decision threshold → Proceed
- If EV < 0 or high uncertainty → Gather more evidence or pass
- If close call → Run a small pilot or reversible test first

**Document:**
- Updated probability: [X%]
- Expected value: [$Y or Z units]
- Decision: [Go / No-Go / Test First]
- Key assumption to monitor: [What could change this?]
- Review date: [When to reassess]

---

## Common Pitfalls

### 1. **Ignoring Base Rates**
- ❌ "Our product is special, so industry benchmarks don't apply"
- ✅ Start with base rates, then adjust based on specific evidence

### 2. **Double-Counting Evidence**
- ❌ Treating correlated evidence as independent
- ✅ If two pieces of evidence come from the same source, use only one or discount heavily

### 3. **Overconfidence in Weak Evidence**
- ❌ Treating anecdotes or small samples as strong evidence
- ✅ Grade evidence quality explicitly and adjust LR accordingly

### 4. **Anchoring on Initial Belief**
- ❌ Refusing to update despite strong contradictory evidence
- ✅ Let the math guide you; if evidence is strong, update significantly

### 5. **Fake Precision**
- ❌ "The probability is exactly 73.4%"
- ✅ Use ranges: "60-80% likely" when uncertainty is high

---

## Integration with CEO Decision Process

**When to trigger Bayesian analysis:**
- CEO says: "What are the odds of X happening?"
- Decision involves uncertain outcomes with measurable evidence
- Multiple pieces of evidence need to be combined systematically
- Prior beliefs exist but new data is emerging

**How to present:**
1. Start with the prior (baseline belief)
2. Show each piece of evidence and its quality grade
3. Calculate updated probability step-by-step
4. Run sensitivity analysis
5. Translate to expected value and decision recommendation
6. Identify what new evidence would most change the conclusion

**Output Format:**
```
## Bayesian Decision Analysis: [Decision Title]

### Hypothesis
[Clear statement of what we're predicting]

### Prior Belief
- Probability: [X%]
- Source: [Industry benchmark / Expert judgment / Historical data]
- Confidence: [High/Medium/Low]

### Evidence Summary
1. [Evidence 1] — Grade: [A/B/C/D] — LR: [X] — [Supports/Contradicts]
2. [Evidence 2] — Grade: [A/B/C/D] — LR: [Y] — [Supports/Contradicts]
3. [Evidence 3] — Grade: [A/B/C/D] — LR: [Z] — [Supports/Contradicts]

### Updated Belief
- Prior: [X%] → Posterior: [Y%]
- Confidence change: [Increased/Decreased/Stable]

### Sensitivity Analysis
- Best case: [A%]
- Base case: [B%]
- Worst case: [C%]
- Decision robust? [Yes/No]

### Expected Value
- EV(Go): [$X]
- EV(No-Go): [$Y]
- Recommendation: [Action]

### What Would Change This?
- If [condition], probability would shift to [Z%]
- Key assumption to monitor: [X]
- Review date: [When]
```

---

## Quick Reference: When to Use Which Method

| Situation | Method | Why |
|-----------|--------|-----|
| Single yes/no decision with one key evidence | Direct Bayes | Simple and intuitive |
| Multiple independent evidence pieces | Odds form with LR multiplication | Handles multiple updates cleanly |
| Continuous outcome (revenue, users, etc.) | Beta-Binomial or Monte Carlo | Better for ranges |
| High uncertainty, weak evidence | Sensitivity analysis + ranges | Avoid false precision |
| Need to explain to non-technical stakeholders | Odds form with visual | Easier to communicate |

---

## Tools and Scripts

For complex calculations, use:
- `scripts/bayesian_calculator.py` — Automated Bayesian updates
- `scripts/sensitivity_analysis.py` — Test assumption robustness
- `scripts/expected_value.py` — EV calculations with probability distributions

---

## Further Reading

- **Internal References:**
  - `references/frameworks.md` — Other decision frameworks
  - `references/cognitive-debiasing.md` — Avoiding bias in probability estimates
  - `scripts/analysis_tools.py` — Python implementation

- **External Resources:**
  - "Thinking in Bets" by Annie Duke
  - "Superforecasting" by Philip Tetlock
  - "The Signal and the Noise" by Nate Silver
