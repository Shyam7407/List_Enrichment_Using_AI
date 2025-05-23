import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import json

# Loading input CSV
df = pd.read_csv('C:\\Users\\Asus\\OneDrive\\Desktop\\s_work\\input.csv', encoding='latin1')

#Setting OpenRouter API key
OPENROUTER_API_KEY = "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"  

#Normalizing the website URL
def normalize_url(url):
    if not str(url).startswith("http"):
        return "https://" + str(url)
    return str(url)

#Extracting richer text content from homepage
def scrape_homepage_text(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        #Grabbing meta description
        meta = soup.find("meta", {"name": "description"}) or soup.find("meta", {"property": "og:description"})
        meta_content = meta['content'].strip() if meta and meta.get('content') else ''

        #Grabbing text from tags
        text_elements = soup.find_all(['h1', 'h2', 'p'])
        text_content = ' '.join([el.get_text().strip() for el in text_elements if el.get_text().strip()])
        combined = (meta_content + " " + text_content).strip()

        return combined[:4000]  #limit to avoid token issues
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return ""

#Using OpenRouter API to analyze
def analyze_with_openrouter(text):
    if not text.strip():
        return {"summary": "N/A", "automation_pitch": "N/A"}

    prompt = f"""
You are an expert business analyst. Based on the following company homepage content, extract and provide:

1. A detailed summary of what the company does and its core offerings.
2. The type of customers they serve or target market.
3. One realistic and creative AI automation idea that QF Innovate could pitch to improve their operations.

Homepage Content:
\"\"\"
{text}
\"\"\"
    """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",  #can replace this with other supported models
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        reply = res.json()["choices"][0]["message"]["content"].strip()

        # Split into parts
        summary = reply.split("2.")[0].strip() if "2." in reply else reply
        automation = reply.split("3.")[-1].strip() if "3." in reply else "N/A"

        return {
            "summary": summary,
            "automation_pitch": automation
        }

    except Exception as e:
        print(f"⚠️ OpenRouter API error: {e}")
        return {"summary": "N/A", "automation_pitch": "N/A"}

#Loop over all companies
summaries = []
automations = []

for index, row in df.iterrows():
    url = normalize_url(row.get("website", ""))
    print(f"\n🔍 Scraping and analyzing: {url}")

    homepage_text = scrape_homepage_text(url)
    print(f"📝 Homepage preview (first 300 chars):\n{homepage_text[:300]}")

    result = analyze_with_openrouter(homepage_text)
    summaries.append(result["summary"])
    automations.append(result["automation_pitch"])

    time.sleep(3)  # Respect rate limits

# Adding to DataFrame and export
df["summary_from_llm"] = summaries
df["automation_pitch_from_llm"] = automations

df.to_csv("enriched_output_openrouter.csv", index=False)
print("✅ All done! Output saved to enriched_output_openrouter.csv")





