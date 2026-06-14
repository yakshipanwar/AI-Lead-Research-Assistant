import pandas as pd
import os


def export_company_report(
    company_name,
    result,
    score,
    reasoning
):

    os.makedirs(
        "exports",
        exist_ok=True
    )

    filename = f"exports/{company_name}.csv"

    data = {

        "Company": [company_name],

        "Industry": [
            result.get("industry", "")
        ],

        "Company Summary": [
            result.get(
                "company_summary",
                ""
            )
        ],

        "Products & Services": [
            ", ".join(
                result.get(
                    "products_services",
                    []
                )
            )
        ],

        "AI Opportunities": [
            ", ".join(
                result.get(
                    "ai_opportunities",
                    []
                )
            )
        ],

        "Lead Score": [score],

        "Score Reasoning": [
            reasoning
        ],

        "Outreach Email": [
            result.get(
                "outreach_email",
                ""
            )
        ]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        filename,
        index=False
    )

    return filename