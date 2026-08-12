# Judicial Bail Predictor
Try it out now !!    https://constitutional-systemm.streamlit.app/

A Streamlit app that gives a preliminary, rule-based assessment of bail eligibility factors for a case, based on common mitigating and aggravating criteria used in Indian criminal procedure. Built with Python and Pandas.

## What it does

You enter case details — the offence, maximum punishment, and mitigating factors like clean antecedents, chargesheet status, time already served, and jail conduct and the app:

- Computes a weighted eligibility score out of 12
- Classifies the case into a status band (Highly Favourable → Adverse) with a suggested bail category
- Lists which specific factors contributed favorably to the score
- References relevant legal provisions and precedent cases commonly cited in bail matters
- Generates a downloadable CSV score matrix and a plain-text summary report

## How it works

The score is built from a fixed, transparent rule set not a trained model so every point is traceable to a specific case fact.

| Factor | Condition | Points |
|---|---|---|
| Punishment length | ≤ 5 years | +4 |
| | ≤ 7 years | +3 |
| | ≤ 10 years | +2 |
| Clean antecedents | First-time offender | +2 |
| Chargesheet filed | Investigation complete | +2 |
| Time served | ≥ 8 months | +2 |
| | ≥ 4 months | +1 |
| Jail conduct | Good behavior recorded | +1 |

**Score → status mapping:**

| Score | Status | Category |
|---|---|---|
| ≥ 9 | Highly Favourable | Regular Bail |
| 7–8 | Favourable | Regular/Interim |
| 5–6 | Conditional | Anticipatory Bail |
| 3–4 | Challenging | Exceptional grounds |
| < 3 | Adverse | Strong opposition |

A confidence percentage is derived directly from the score (`70 + score × 2`, capped at 95%) to indicate how far the case sits from the assessment boundaries, not a statistical certainty measure.

## Tech stack

- Python
- Streamlit
- Pandas

## Running it locally

```
pip install streamlit pandas numpy
streamlit run app.py
```

Then open `http://localhost:8501`, fill in the case profile and mitigating factors, and click **Execute Judicial Assessment**.

## Inputs

- **Case profile**: offence type, maximum punishment (years)
- **Mitigating factors**: clean antecedents, chargesheet filed, months of detention already served, jail conduct

## Outputs

- Eligibility score and confidence percentage
- Status classification and suggested bail category
- List of favorable factors identified
- Referenced statutory provisions and precedent cases
- Downloadable CSV score matrix and text-format assessment report

## Important disclaimer

This tool produces an **algorithmic, rule-based preliminary indication only** it is not legal advice and does not represent the actual reasoning a court would apply. Real bail decisions weigh case-specific facts, judicial discretion, and considerations far beyond a fixed points system. The legal precedents referenced are shown for context, not as a substitute for consulting a qualified legal professional. Final authority always rests with the court.

## Limitations

- The scoring weights are illustrative defaults, not derived from statistical analysis of actual case outcomes
- The tool does not account for offence-specific nuances, jurisdictional variation, or judge-specific tendencies
- Legal precedents shown are static references, not dynamically matched to the specific case facts entered
- Should be treated as an educational/demonstrative tool, not a decision-support system for real proceedings

## Project structure

```
├── app.py
├── requirements.txt
```
