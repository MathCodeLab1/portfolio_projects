
import requests
from bs4 import BeautifulSoup
import pandas as pd

# STEP 1: send request to the website
url = "https://books.toscrape.com/"
response = requests.get(url)

# STEP 2: parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# STEP 3: find all book titles
titles = soup.find_all("h3")

print("=== BOOK TITLES ===")
for t in titles:
    print(t.get_text())

# STEP 4: find all price elements
prices = soup.find_all("p", class_="price_color")

print("\n=== BOOK PRICES ===")
for p in prices:
    print(p.get_text().replace("Â", ""))

# STEP 5: Combine titles and prices into a table
books = []
for t, p in zip(titles, prices):
    title_text = t.get_text(strip=True)
    price_text = p.get_text(strip=True).replace("Â", "")
    books.append({"title": title_text, "price": price_text})

df = pd.DataFrame(books)
print("\n=== DATAFRAME PREVIEW ===")
print(df.head())
quit()
# STEP 6: Save to CSV file
df.to_csv("books_page1.csv", index=False)
print("\nSaved to books_page1.csv")


