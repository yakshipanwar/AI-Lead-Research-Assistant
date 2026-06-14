def calculate_lead_score(company_data):

    score = 0

    industry = company_data.get(
        "industry",
        ""
    ).lower()

    summary = company_data.get(
        "company_summary",
        ""
    )

    products = company_data.get(
        "products_services",
        []
    )

    ai_opportunities = company_data.get(
        "ai_opportunities",
        []
    )

    # ----------------------
    # Industry Score (20)
    # ----------------------

    tech_keywords = [
        "software",
        "technology",
        "saas",
        "ai",
        "cloud",
        "it"
    ]

    if any(
        keyword in industry
        for keyword in tech_keywords
    ):
        score += 20

    elif industry:
        score += 10

    # ----------------------
    # Products Score (20)
    # ----------------------

    if len(products) >= 5:
        score += 20

    elif len(products) >= 3:
        score += 15

    elif len(products) >= 1:
        score += 10

    # ----------------------
    # AI Opportunity Score (30)
    # ----------------------

    if len(ai_opportunities) >= 3:
        score += 30

    elif len(ai_opportunities) == 2:
        score += 20

    elif len(ai_opportunities) == 1:
        score += 10

    # ----------------------
    # Company Summary Quality (20)
    # ----------------------

    summary_length = len(summary)

    if summary_length > 300:
        score += 20

    elif summary_length > 150:
        score += 15

    elif summary_length > 50:
        score += 10

    # Maximum 100

    return min(score, 100)


def score_reasoning(score):

    if score >= 85:
        return (
            "Excellent lead with strong digital maturity, "
            "clear AI adoption opportunities and high business value."
        )

    elif score >= 70:
        return (
            "Strong lead with good AI potential and multiple areas "
            "where automation or intelligence can create value."
        )

    elif score >= 50:
        return (
            "Moderate lead with some AI opportunities but requires "
            "further qualification."
        )

    else:
        return (
            "Lower priority lead due to limited business information "
            "or fewer identifiable AI opportunities."
        )