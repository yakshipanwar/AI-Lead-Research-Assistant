import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_company(company_name, website_content):
    """
    Analyze company using Gemini and return structured JSON.
    """

    prompt = f"""
You are an expert B2B sales research assistant.

Analyze the company based on the information provided.

Company Name:
{company_name}

Website Content:
{website_content}

Return ONLY valid JSON.

Rules:
- Return ONLY JSON
- No markdown
- No code blocks
- No explanations
- company_summary should be 2-3 sentences
- products_services should contain 3-5 items
- ai_opportunities must contain EXACTLY 3 items
- outreach_email must be professional and under 150 words
- lead_score should NOT be included

Required JSON format:

{{
    "industry": "",
    "company_summary": "",
    "products_services": [
        "",
        "",
        ""
    ],
    "ai_opportunities": [
        "",
        "",
        ""
    ],
    "outreach_email": ""
}}
"""

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove markdown if Gemini adds it
        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {
            "industry": "Unknown",
            "company_summary": f"Error: {str(e)}",
            "products_services": [],
            "ai_opportunities": [],
            "outreach_email": ""
        }