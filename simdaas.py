import requests
from bs4 import BeautifulSoup
import csv

url = "https://simdaas.com/about-us/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

about_us = soup.find("h1").get_text(strip=True)

welcome = soup.find("h2").get_text(strip=True)

our_team = "Yes" if soup.find("h2", string=lambda x: x and "Our Team" in x) else "No"

product_link = "Yes" if soup.find("a", string=lambda x: x and "Products" in x) else "No"

print("About Us Page:", about_us)
print("Welcome Section:", welcome)
print("Our Team:", our_team)
print("Product Link:", product_link)
print("Page URL:", url)

with open("simdaas_about.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "About Us Page",
        "Welcome To SimDaaS",
        "Our Team",
        "Product Link",
        "Page URL"
    ])

    writer.writerow([
        about_us,
        welcome,
        our_team,
        product_link,
        url
    ])

print("CSV created successfully.")