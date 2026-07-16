from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import re
import time

driver = webdriver.Chrome()

url = "https://www.vedantu.com/neet/neet-previous-year-question-paper"
driver.get(url)

time.sleep(8)

rows = []

# Page ke saare links
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    try:
        text = link.text.strip()

        if "Question Paper" in text:

            href = link.get_attribute("href")

            year_match = re.search(r"20\d{2}", text)
            year = year_match.group() if year_match else ""

            rows.append([
                year,
                text,
                href
            ])

    except Exception:
        pass

driver.quit()

# CSV Save
with open("neet_papers.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Year",
        "Paper Name",
        "Paper URL"
    ])

    writer.writerows(rows)

print(f"{len(rows)} records saved successfully.")