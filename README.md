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
