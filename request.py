import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
def multi_page(SEARCH_QUERY,NUM_PAGES):

 for page in range(1, NUM_PAGES + 1):
    url = f"https://www.amazon.com/s?k={SEARCH_QUERY}&page={page}"
    print(f"Scraping page {page}...")
    driver.get(url)
    time.sleep(random.uniform(3, 6))
    soup = BeautifulSoup(driver.page_source, "lxml")
    products = soup.select("div[data-component-type='s-search-result']")
    for product in products:
        title_tag = product.select_one("h2 span")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        price_tag = product.select_one("span.a-price span.a-offscreen")
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        rating_tag = product.select_one("span.a-icon-alt")
        rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"
        reviews_tag = product.select_one("span[aria-label$=' ratings']")
        reviews = reviews_tag.get_text(strip=True) if reviews_tag else "N/A"
        all_results.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Reviews": reviews,
            "query": SEARCH_QUERY
        })
    time.sleep(random.uniform(2, 5)) 


SEARCH_QUERY = ["laptop", "headphones", "smartphone"]
NUM_PAGES = 3
OUTPUT_FILE = "amazon_products.csv"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
all_results = []
for query in SEARCH_QUERY:
 multi_page(query, NUM_PAGES)
driver.quit()
df = pd.DataFrame(all_results)
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
print(f"Scraping completed. {len(all_results)} products saved to {OUTPUT_FILE}.")
