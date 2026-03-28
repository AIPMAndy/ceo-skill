# CEO Decision Frameworks — Detailed Reference

Load this file when you need detailed instructions on applying a specific framework.

---

## 1. Decision Matrix (Weighted Scoring)

**When to use:** Choosing between 2-5 mutually exclusive options with multiple criteria.

**Process:**
1. List criteria that matter (e.g., cost, speed, risk, strategic fit, team capability)
2. Assign weight to each criterion (must sum to 100%)
3. Score each option on each criterion (1-10)
4. Calculate weighted total
5. Sensitivity check: flip the top-2 weights — does the winner change?

**Output format:**

| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| Revenue Impact | 30% | 8 (2.4) | 6 (1.8) | 7 (2.1) |
| Risk Level | 25% | 4 (1.0) | 8 (2.0) | 6 (1.5) |
| Speed to Market | 20% | 9 (1.8) | 5 (1.0) | 7 (1.4) |
| Team Readiness | 15% | 7 (1.05)| 9 (1.35)| 6 (0.9) |
| Strategic Fit | 10% | 8 (0.8) | 7 (0.7) | 9 (0.9) |
| **Total** | | **7.05** | **6.85** | **6.80** |

⚠️ **Warning:** If scores are within 10% of each other, the matrix isn't decisive — use a different approach.

---

## 2. Pre-Mortem Analysis

**When to use:** Before committing to a major decision. Especially good for Type 1 (irreversible) decisions.

**Process:**
1. Assume it's 12 months from now and the decision was a **complete disaster**
2. Ask: "What went wrong?" — brainstorm every failure mode
3. Categorize failures: Predictable vs Black Swan, Internal vs External
4. For each failure mode: What's the probability? What's the early warning sign?
5. Create monitoring plan for top 5 risks

**Output format:**
```
| Failure Mode | Probability | Impact | Early Warning Sign | Mitigation |
|---|---|---|---|---|
| Key engineer quits | 30% | High | Disengagement in meetings | Retention package now |
| Market shifts before launch | 15% | Critical | Competitor announcement | Faster MVP, monthly review |
```

---

## 3. Expected Value (EV) Analysis

**When to use:** When outcomes can be quantified and probabilities estimated.

**Formula:** EV = Σ (Probability × Outcome Value)

**Process:**
1. List all possible outcomes for each option
2. Estimate probability of each outcome (must sum to 100%)
3. Estimate financial value of each outcome
4. Calculate EV
5. Also calculate downside risk (worst realistic case × its probability)

**Example:**
```
Option A: Launch new product
- Success (40%): +$5M → EV contribution: +$2M
- Moderate (35%): +$1M → EV contribution: +$350K
- Failure (25%): -$2M → EV contribution: -$500K
Total EV: +$1.85M

Option B: Expand existing product
- Success (60%): +$2M → EV contribution: +$1.2M
- Moderate (30%): +$800K → EV contribution: +$240K  
- Failure (10%): -$500K → EV contribution: -$50K
Total EV: +$1.39M
```

⚠️ **Note:** EV favors Option A, but Option B has much lower downside risk. Present both perspectives.

---

## 4. ICE Scoring (Impact, Confidence, Ease)

**When to use:** Prioritizing a backlog of initiatives, features, or projects.

**Process:**
1. Score each initiative: Impact (1-10), Confidence (1-10), Ease (1-10)
2. ICE = Impact × Confidence × Ease
3. Sort descending
4. Apply resource constraints (mark which ones fit in current capacity)
5. Check for dependencies (some items unlock others)

**Scoring guide:**
- **Impact**: How much does this move the needle on our #1 goal?
- **Confidence**: How sure are we about the impact estimate?
- **Ease**: How easy/fast is this relative to our capacity?

---

## 5. Porter's Five Forces

**When to use:** Evaluating market entry, competitive positioning, or industry attractiveness.

**The Five Forces:**
1. **Threat of New Entrants** — How easy is it for others to enter? (Capital requirements, regulation, network effects, brand loyalty)
2. **Bargaining Power of Suppliers** — Can suppliers squeeze our margins? (Concentration, switching costs, substitutes)
3. **Bargaining Power of Buyers** — Can customers demand lower prices? (Concentration, price sensitivity, switching costs)
4. **Threat of Substitutes** — What alternative solutions exist? (Price-performance of substitutes, switching costs)
5. **Competitive Rivalry** — How intense is competition? (Number of competitors, growth rate, differentiation, exit barriers)

**Score each force:** Weak (favorable) / Moderate / Strong (unfavorable)
**Overall assessment:** Attractive / Neutral / Unattractive industry

---

## 6. OODA Loop (Crisis Response)

**When to use:** Time-critical situations requiring rapid decision cycles.

**Cycle (repeat until stable):**
1. **OBSERVE** — What are the facts? (Not rumors, not assumptions — verified facts only)
   - What happened?
   - Who is affected?
   - What's the blast radius?
   - What do we NOT know yet?

2. **ORIENT** — What does this mean?
   - Severity: 1-10
   - Is this getting worse or stabilizing?
   - What are our available resources right now?
   - Have we seen this pattern before?

3. **DECIDE** — What's our move?
   - Minimum viable response (next 2 hours)
   - Short-term stabilization (next 24 hours)
   - Root cause fix (next 1-2 weeks)

4. **ACT** — Execute and observe results
   - Assign clear owners
   - Set check-in time
   - Prepare next OODA cycle

---

## 7. Force Field Analysis

**When to use:** Evaluating organizational change, new processes, or cultural shifts.

**Process:**
1. Define the desired change
2. List **Driving Forces** (things pushing toward change)
3. List **Restraining Forces** (things resisting change)
4. Score each force (1-5 strength)
5. Strategy: Either strengthen drivers or weaken restrainers (usually weakening restrainers is easier)

**Visual format:**
```
DRIVING FORCES          ←  Current State  →          RESTRAINING FORCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Market demand [████▒]  5                    4  [▒████] Legacy systems
Cost savings  [███▒▒]  3                    5  [█████] Cultural resistance  
Tech ready    [████▒]  4                    2  [▒▒███] Training cost
CEO mandate   [█████]  5                    3  [▒████] Middle mgmt inertia
              --------                         --------
Total:           17                              14     → Net: +3 (Change favored)
```

---

## 8. Scenario Planning

**When to use:** Strategic decisions with high uncertainty and long time horizons.

**Process:**
1. Identify the 2 most impactful uncertain variables
2. Create a 2×2 matrix with extreme values of each variable
3. Name each quadrant (make it memorable)
4. For each scenario:
   - What does the world look like?
   - How does our decision perform?
   - What early signals would tell us we're in this scenario?
5. Choose the option that performs acceptably across most scenarios (robust strategy)

---

## 9. Opportunity Cost Framework

**When to use:** When saying YES to something means saying NO to something else.

**Process:**
1. What are we saying YES to? (Time, money, attention)
2. What are we implicitly saying NO to? (List specific alternatives)
3. For each NO: What's the expected value we're giving up?
4. Is the YES worth more than the best NO?

**Key question:** "If we weren't already doing X, would we start it today?"
(If no → it's a candidate for killing, regardless of sunk costs.)

---

## 10. Regret Minimization Framework (Bezos Test)

**When to use:** Big life/company decisions where quantitative analysis falls short.

**Process:**
1. Project yourself to age 80 (or 10 years from now)
2. Ask: "Will I regret NOT doing this?"
3. Ask: "Will I regret DOING this?"
4. The option with minimum long-term regret wins

**Best for:** Decisions about starting new ventures, taking bold bets, or walking away from something comfortable.
