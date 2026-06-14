from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from scraper import scrape_website
from ai_service import analyze_company
from lead_score import (
    calculate_lead_score,
    score_reasoning
)

from export_utils import (
    export_company_report
)

app = Flask(__name__)

latest_result = {}


@app.route("/", methods=["GET", "POST"])
def home():

    global latest_result

    result = None
    score = None
    reasoning = None
    error = None

    company_name = None
    website_url = None

    if request.method == "POST":

        try:

            company_name = request.form.get(
                "company_name"
            )

            website_url = request.form.get(
                "website_url"
            )

            scraped_data = scrape_website(
                website_url
            )

            content = scraped_data.get(
                "content",
                ""
            )

            if not content.strip():

                content = f"""
                Company Name: {company_name}
                Website: {website_url}
                """

            result = analyze_company(
                company_name,
                content
            )

            score = calculate_lead_score(
                result
            )

            reasoning = score_reasoning(
                score
            )

            latest_result = {
                "company_name": company_name,
                "website_url": website_url,
                "result": result,
                "score": score,
                "reasoning": reasoning
            }

        except Exception as e:

            error = str(e)

    return render_template(
        "index.html",
        result=result,
        score=score,
        reasoning=reasoning,
        error=error,
        company_name=company_name,
        website_url=website_url
    )


@app.route("/export")
def export_csv():

    global latest_result

    if not latest_result:
        return "No report available."

    filepath = export_company_report(

        latest_result["company_name"],

        latest_result["result"],

        latest_result["score"],

        latest_result["reasoning"]

    )

    return send_file(
        filepath,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )