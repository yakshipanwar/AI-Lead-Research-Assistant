from ai_service import analyze_company
from lead_score import (
    calculate_lead_score,
    score_reasoning
)

result = analyze_company(
    "Python",
    """
    Python is used for web development,
    AI, automation and data science.
    """
)

score = calculate_lead_score(result)

print(score)
print(score_reasoning(score))