<div align="center">

# 🧠 CEOskill

**Make AI think like a world-class CEO chief of staff: structure decisions, detect bias, predict competition, manage stakeholders.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Skill](https://img.shields.io/badge/Type-Agent%20Skill-blue)](./SKILL.md)
[![Language](https://img.shields.io/badge/Python-helpers-3776AB?logo=python&logoColor=white)](./scripts/analysis_tools.py)

[简体中文](./README.md) | **English**

</div>

---

## One Line

**AI gives advice easily. But decomposing trade-offs, detecting cognitive bias, predicting competitive responses, and navigating stakeholder dynamics — that's the decision quality CEOs actually need.**

## 5-Second Fit Check

If you face these problems regularly, this is built for you:

| Scenario | Typical Questions |
|----------|------------------|
| 🎯 **Strategic Decisions** | Enter a new market? Build or acquire? Keep investing or cut losses? |
| 💰 **Resource Allocation** | 5 projects, budget for 2 — which ones? Growth vs product vs org? |
| 🔥 **Crisis Response** | CTO leaving for a competitor — what do you do in 2 hours? |
| 🤝 **Stakeholder Management** | How to align board, investors, and leadership? Manage reorg politics? |
| ⚔️ **Competitive War Gaming** | If we cut prices / launch a feature, how will competitors react? |

## The Problem: Why Generic AI Advisors Fall Short

Most "CEO advisor" AI prompts share the same weaknesses:

```
User: "Should we enter the Japan market?"

Generic AI:
"Entering the Japan market is an important strategic decision. You should
consider market size, competitive landscape, localization costs, and
regulatory requirements. I recommend conducting market research, assessing
risks, and developing a detailed plan. Would you like me to help you
identify some key questions to consider?"

❌ Sounds polished but stays vague
❌ Lists frameworks but doesn't choose the right one
❌ Gives advice without surfacing trade-offs
❌ Doesn't check cognitive bias (are you chasing FOMO because a competitor entered?)
❌ Doesn't predict competitive response (how will local players fight back?)
❌ Doesn't map stakeholders (who on your board supports vs opposes this?)
```

## The Solution: How CEOskill Works

```
User: "Should we enter the Japan market?"

CEOskill:

【Decision Classification】Type 1 (One-Way Door) — High entry cost, high exit cost

【Bias Check】
- Are you experiencing FOMO because a competitor just entered?
- Are you overestimating first-mover advantage? (Japan rewards localization depth)
- Are you underestimating regulatory/cultural barriers?

【4 Options + Trade-offs】
A. Wholly-owned subsidiary ($5M, 18-month payback, risk: localization failure)
B. JV / acquire local player ($8M, 6-month launch, risk: integration conflict)
C. Lightweight pilot ($500K, validate PMF first, risk: miss the window)
D. Don't enter (save $5M+, focus current markets, risk: competitor builds moat)

【Competitive War Gaming】
- How will the top 3 local players respond? (Price war / channel lockout / regulatory lobbying)
- What does your competitor's performance look like 6 months after entry? (User growth vs burn rate)

【Stakeholder Map】
- Board: 2 support (bullish on international), 1 opposes (fears resource dilution)
- Investors: care about 18-month ARR growth, geography-agnostic
- Leadership: VP Sales supports, CFO neutral-leaning-against

【Recommendation】
Option C (pilot) + 6-month decision gate.
Rationale: Japan PMF uncertainty is high; going all-in is premature.
Next Steps:
1. Find 1-2 local design partners (2 weeks)
2. Run MVP to validate willingness to pay (3 months)
3. Data-driven decision on A/B/D (month 6)

✅ Structured decision workflow
✅ At least 3 comparable options + do nothing
✅ Explicit trade-offs
✅ Cognitive bias check
✅ Competitive + stakeholder response prediction
✅ Next steps + decision gate
```

## CEOskill vs Generic AI Advisors

| Capability | Generic AI | Consultant Prompt | **CEOskill** |
|------------|-----------|-------------------|--------------|
| Decision classification (one-way / two-way / crisis) | ❌ | ⚠️ Sometimes | ✅ Enforced |
| At least 3 options + do nothing | ❌ | ⚠️ Inconsistent | ✅ Enforced |
| Explicit trade-offs (not just conclusions) | ❌ | ⚠️ | ✅ |
| Cognitive debiasing (FOMO / sunk cost / anchoring) | ❌ | ❌ | ✅ |
| Competitive response prediction (war gaming) | ❌ | ⚠️ | ✅ |
| Stakeholder mapping (board / investors / leadership) | ❌ | ⚠️ | ✅ |
| Quantitative analysis (Monte Carlo / ICE / NPV) | ❌ | ❌ | ✅ |
| Crisis / Prioritization / War Game modes | ❌ | ❌ | ✅ |

## Core Capabilities

### 1. Structured Decision Workflow

Not "giving advice" — **decomposing decisions**:

- **Decision classification**: One-Way Door / Two-Way Door / Crisis / Strategic Bet
- **Framework selection**: Automatically picks the best framework for the scenario
- **Option generation**: Forces at least 3 comparable options + do nothing
- **Trade-off analysis**: Explicit cost, risk, and resource requirements for each option

### 2. Cognitive Debiasing

The biggest enemy of CEO decisions is not lack of information — it's cognitive bias:

- **Anchoring**: Are you anchored to a number set by a competitor / investor / advisor?
- **Sunk cost**: Are you continuing because "we already spent $X on this"?
- **Confirmation bias**: Are you only looking for data that supports your preferred option?
- **FOMO**: Are you doing this because "everyone else is"?
- **Availability bias**: Are you overweighting a recent vivid event?

See: [`references/cognitive-debiasing.md`](./references/cognitive-debiasing.md)

### 3. Competitive War Gaming

Don't just analyze yourself — predict the opponent:

- **If we cut prices, will competitors match or differentiate?**
- **If we enter their market, will they counterattack or play defense?**
- **If we acquire this company, how will competitors respond?**

See: [`references/war-gaming.md`](./references/war-gaming.md)

### 4. Stakeholder Playbook

Executive decisions aren't just about "right vs wrong" — they're about "who supports vs who opposes":

- **Board**: Who is your ally? Who opposes? Who is the swing vote?
- **Investors**: What metrics do they care about? What's their tolerance?
- **Leadership team**: Who benefits / loses from this decision?
- **Key employees**: Who might leave because of this?

See: [`references/stakeholder-playbook.md`](./references/stakeholder-playbook.md)

### 5. Quantitative Analysis Tools

Not just qualitative — quantitative support built in:

- **Monte Carlo simulation**: Probability distributions under uncertainty
- **ICE scoring**: Impact / Confidence / Ease for quick prioritization
- **NPV / IRR**: Investment return analysis
- **Expected Value**: Probability-weighted outcome calculation
- **Scenario Planning**: Best / base / worst case analysis

See: [`scripts/analysis_tools.py`](./scripts/analysis_tools.py)

## Use Cases

### Strategic Decisions
- Enter a new market? Acquire or build? Cut losses or keep investing?
- Example: [M&A Acquisition Decision](./examples/mna-acquisition-decision.md)

### Resource Allocation
- Multiple projects competing for resources. Which first? How to split budget?
- Example: [5-Initiative Prioritization](./examples/prioritization-five-initiatives.md)

### Crisis Response
- Key executive departure, production outage, PR crisis — what to do first?
- Example: [CTO Departure Crisis](./examples/cto-departure-crisis.md)

### Competitive War Gaming
- If we do X, how will competitors respond?

More examples: [`examples/`](./examples/)

## Quick Start

### Just Ask

Treat it as your CEO chief of staff:

```
"Should we enter the Japan market?"
"5 projects, budget for 2 — how to prioritize?"
"CTO is leaving for a competitor. What do I do in the next 2 hours?"
"If we cut prices 20%, how will competitors respond?"
```

### What to Expect

Not generic advice, but:

1. **Decision classification** — What type of decision is this? Why does it matter?
2. **Bias check** — What are your blind spots?
3. **Option comparison** — At least 3 options + do nothing, with trade-offs
4. **Competitive / stakeholder analysis** — How will others react?
5. **Recommendation + Next Steps** — What to do, and what comes next?

## Installation

### OpenClaw / Claude Code / Cursor

Load `SKILL.md` directly:

```bash
# OpenClaw
openclaw skill install https://github.com/AIPMAndy/CEOskill

# Claude Code / Cursor
Add SKILL.md to your project context
```

### Other Agent Runtimes

See: [RUNTIME.md](./RUNTIME.md)

Core principle:
- Text-only runtimes can run the basic workflow
- Web search makes strategic output stronger
- Python / code execution unlocks quantitative analysis

## Repository Structure

```text
.
├── SKILL.md                            # Main skill definition (core)
├── references/
│   ├── frameworks.md                   # Decision framework library
│   ├── cognitive-debiasing.md          # Cognitive bias detection
│   ├── stakeholder-playbook.md         # Stakeholder management
│   └── war-gaming.md                   # Competitive simulation
├── scripts/analysis_tools.py           # Quantitative analysis tools
├── examples/                           # Real-world cases
│   ├── mna-acquisition-decision.md
│   ├── cto-departure-crisis.md
│   └── prioritization-five-initiatives.md
└── evals/evals.json                    # Evaluation cases
```

## Roadmap

- [x] Main skill definition
- [x] Decision framework references
- [x] Cognitive debiasing
- [x] Stakeholder playbook
- [x] War gaming
- [x] Analysis tools
- [ ] Add 10+ real-world cases (M&A / layoffs / fundraising / reorg)
- [ ] Add benchmark / eval results
- [ ] Add video demos
- [ ] Add more Agent Runtime adapters

## Contributing

Contributions welcome:

- Real decision cases (anonymized)
- New decision frameworks
- Stronger eval cases
- Agent Runtime adapters

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

## License

MIT License.

## If This Helps You

1. Give the repo a **⭐ Star**
2. Submit a real decision case or PR
3. Share with someone who needs it

**Turn AI decision support from a personal tool into a reusable decision toolkit.**

---

<div align="center">

Made with 🧠 by [Andy](https://github.com/AIPMAndy)

</div>
