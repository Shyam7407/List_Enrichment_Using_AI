📂 File Overview

##This project includes both a web interface and a script version:

- `app.py` — A Streamlit-based web app for uploading and enriching CSVs.
- `QF_innovate_assessmnent[1].py` — A standalone Python script that performs the same enrichment from the command line.

You can use either based on your preference:
- Use `app.py` for a user-friendly web experience.
- Use `QF_innovate_assessmnent.py` if you prefer automation or batch processing.

# AI_Automation
Lead Enrichment Automation Tool (QF Innovate Assessment)

This Python project enriches a list of companies with LLM-generated summaries and AI automation ideas by scraping company homepages and analyzing the text using OpenRouter-powered GPT-3.5-turbo.

##  Features

-  Scrapes homepage content from company websites.
-  Summarizes what each company does.
-  Suggests a unique AI automation pitch for QF Innovate to offer.
-  Outputs a CSV with enriched data.

## 📁 Input CSV Format

Your input CSV should contain at least one column named `website`.

Example:
| company_name | website             |
|--------------|---------------------|
| OpenAI       | www.openai.com      |
| DeepMind     | www.deepmind.com    |

##  Output CSV Columns

The enriched output will contain:
- `summary_from_llm` — summary of the company
- `automation_pitch_from_llm` — a relevant AI automation idea

## 🔧 How It Works

1. Loads input CSV using `pandas`
2. For each row:
   - Normalizes the URL
   - Scrapes homepage content
   - Sends the text to OpenRouter’s LLM (GPT-3.5-turbo)
   - Parses the model’s structured response
3. Appends new columns and saves to CSV.

## 🛠 Setup

Install required packages:

pip install pandas requests beautifulsoup4


# Streamlit_UI
                   #LLM-Powered Company Lead Enrichment Tool (QF Innovate Assessment)
This project is a Streamlit-based web application that enriches company leads by scraping their homepage and analyzing the content using an LLM API via OpenRouter.

🚀 Features
Uploaded a CSV with company websites.

Automatically scrape homepage text using BeautifulSoup.

Send extracted content to OpenRouter (e.g., gpt-3.5-turbo) for:

A company summary

An AI automation pitch for QF Innovate

Preview enriched results in a table.

Download the enriched CSV.

📁 Input Format
Your CSV file must include a column named website.

Example:

company_name	website
Zoho	www.zoho.com

📤 Output Columns
summary_from_llm — What the company does.

automation_pitch_from_llm — A tailored AI idea QF Innovate can pitch.

🛠 Requirements
Install dependencies:
pip install streamlit pandas requests beautifulsoup4
🔐 Configuration
Got free API key from https://openrouter.ai

In app.py, replace the placeholder key:

OPENROUTER_API_KEY = "sk-or-xxxxxxxxxxxxxxxxxxxx"
▶️ How to Run the App
streamlit run app.py
It will launch a local browser window with the web interface.

💡 Notes
The tool uses only <p> tags. You can modify scrape_homepage_text() to include <h1>, <h2>, etc.

API usage is rate-limited. A time.sleep(3) is added after each request.

If homepage content is very short or blocked by JavaScript, the result might be N/A.

#NOTE🥇
▶️ How to Run the App
streamlit run app.py In Terminal

Video Link:-
https://drive.google.com/drive/folders/1FpnkCIjHXixgxl1Mj_5VOuJNZ9PXlx_1?usp=sharing



