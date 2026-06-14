# AI Lead Research Assistant

An AI-powered sales intelligence application that researches companies, identifies AI opportunities, calculates lead scores, and generates personalized outreach emails.

## Project Overview

Sales teams often spend significant time researching potential clients before initiating outreach. This project automates that process by combining web scraping, AI-powered analysis, lead scoring, and personalized email generation into a single workflow.

Given a company name and website URL, the application:

* Extracts publicly available company information
* Generates a company summary
* Identifies the industry
* Extracts products and services
* Suggests relevant AI opportunities
* Calculates a lead score (1–100)
* Generates a personalized cold outreach email
* Exports results as a CSV report

---

## Features

### Company Research

* Website scraping using Requests and BeautifulSoup
* Automatic extraction of company information

### AI-Powered Analysis

Using Google Gemini API to generate:

* Industry classification
* Company summary
* Products and services offered
* AI opportunities
* Personalized outreach email

### Lead Scoring Engine

Custom rule-based lead scoring based on:

* Industry relevance
* Product diversity
* AI adoption potential
* Business information quality

### CSV Export

Export generated reports for future sales and business development activities.

### Modern Dashboard

* Responsive Tailwind CSS interface
* Lead score visualization
* Company insights dashboard
* Professional report layout

### Containerized Deployment

* Docker support
* Docker Compose support
* Environment-based configuration

---

## Tech Stack

### Backend

* Python
* Flask

### AI Layer

* Google Gemini API
* ### AI Provider Note

Google Gemini API was used during development and testing. The application architecture remains provider-agnostic, and the AI service layer can be switched to OpenAI or Anthropic Claude by modifying only the `ai_service.py` module. Gemini was selected for implementation due to development-time API availability while maintaining the same overall workflow and design principles required for the assignment.


### Web Scraping

* Requests
* BeautifulSoup4

### Frontend

* HTML
* Tailwind CSS

### Data Processing

* Pandas

### Containerization

* Docker
* Docker Compose

---

## Application Workflow

```text
User Input
    ↓
Website Scraper
    ↓
Gemini AI Analysis
    ↓
Lead Scoring Engine
    ↓
Outreach Email Generator
    ↓
Dashboard & CSV Export
```

---

## Project Structure

```text
AI-Lead-Research-Assistant/

├── app.py
├── ai_service.py
├── scraper.py
├── lead_score.py
├── export_utils.py
│
├── templates/
│   └── index.html
│
├── screenshots/
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
│
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yakshipanwar/AI-Lead-Research-Assistant.git

cd AI-Lead-Research-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
source venv/Scripts/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running Locally

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

## Running with Docker

Build and run:

```bash
docker compose up --build
```

Application will be available at:

```text
http://localhost:5000
```

---

## Lead Scoring Logic

The application uses a custom scoring system rather than relying on AI-generated scores.

Factors considered:

| Factor                      | Weight |
| --------------------------- | ------ |
| Industry Relevance          | 20     |
| Product Diversity           | 20     |
| AI Opportunities            | 30     |
| Company Information Quality | 30     |

Maximum Score: **100**

---

## Sample Companies Tested

### Infosys

**Industry:** IT Services & Consulting

**Lead Score:** High

**AI Opportunities:**

* Enterprise AI assistants
* Intelligent automation
* Predictive analytics

---

### Tata Consultancy Services (TCS)

**Industry:** IT Consulting & Digital Transformation

**Lead Score:** High

**AI Opportunities:**

* AI-driven business transformation
* Intelligent document processing
* Enterprise analytics

---

### Zomato

**Industry:** Food Delivery & Restaurant Technology

**Lead Score:** High

**AI Opportunities:**

* Delivery route optimization
* Demand forecasting
* Personalized recommendations

---

## Screenshots

### Homepage
```text
screenshots/homepage.png
<img width="1697" height="632" alt="Homepage" src="https://github.com/user-attachments/assets/7f58a686-5c74-4240-9053-dabfb8022931" />

```

### Infosys Analysis
```text
screenshots/infosys-analysis.png
<img width="847" height="912" alt="infosys-analysis" src="https://github.com/user-attachments/assets/0290d1c0-dfc5-47be-9978-40e6da1edef2" />

```

### Zomato Analysis
```text
screenshots/zomato-analysis.png
<img width="827" height="882" alt="zomato-analysis" src="https://github.com/user-attachments/assets/84b8aa91-74a3-415c-a479-b81a6bc383a6" />
```

---

## Assumptions

* Public website information is sufficient for initial lead research.
* AI opportunities are generated from publicly available business information.
* Lead scores are heuristic-based and intended for lead qualification rather than definitive business valuation.

---

## Future Improvements

* OpenAI and Claude support
* LinkedIn enrichment
* Batch company analysis
* CRM integration
* PDF export
* Agentic multi-step research workflow
* Advanced AI-based lead scoring

---

## Author
**Yakshi Panwar**
Computer Engineering Student | Full Stack Developer | AI Enthusiast
