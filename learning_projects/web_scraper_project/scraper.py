import requests
from bs4 import BeautifulSoup
import pandas as pd

# ---------- MULTI-PAGE SCRAPING ----------
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []   # this will store all scraped rows

# scrape pages 1 to 3 for now (we can extend later)
for page in range(1, 4):
    print(f"\n=== SCRAPING PAGE {page} ===")

    url = base_url.format(page)
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("h3")
    prices = soup.find_all("p", class_="price_color")

    for t, p in zip(titles, prices):
        title_text = t.get_text(strip=True)
        price_text = p.get_text(strip=True).replace("Â", "")   # clean weird char

        # numeric price for analysis
        price_value = float(price_text.replace("£", ""))

        all_books.append({
            "page": page,
            "title": title_text,
            "price": price_text,
            "price_value": price_value
        })

# ---------- CREATE DATAFRAME ----------
df = pd.DataFrame(all_books)

print("\n=== PREVIEW (FIRST 5 ROWS) ===")
print(df.head())


# ---------- SAVE ----------
df.to_csv("books_all_pages.csv", index=False)
print("\nSaved to books_all_pages.csv")


# --- CLEANING ---

# Remove any duplicate rows (just in case)
df = df.drop_duplicates()

# Remove books without title or price (rare)
df = df.dropna(subset=["title", "price_value"])

# Reset index after cleaning
df = df.reset_index(drop=True)

print("\n=== ANALYSIS ===")
print("Total books scraped:", len(df))

print("\nMost expensive 5 books:")
print(df.sort_values("price_value", ascending=False).head()[["title", "price"]])

print("\nCheapest 5 books:")
print(df.sort_values("price_value", ascending=True).head()[["title", "price"]])

df.to_csv("books_all_pages.csv", index=False)
print("\nSaved to books_all_pages.csv")