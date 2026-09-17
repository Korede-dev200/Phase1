import requests

url = "https://books.toscrape.com/catalogue/page-2.html"
response = requests.get(url)
response.encoding = "utf-8"  # page declares UTF-8, but requests defaults to guessing
print(response.status_code)
print(response.text[:500]) # Print the first 500 characters of the response text

from bs4 import BeautifulSoup


soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)
print(soup.title.text)

books = soup.find_all("article", class_="product_pod")
print(len(books))

print(len(response.text))
print("product_pod" in response.text)

import pandas as pd

# List to hold extracted data
scraped_books = []

# Loop through each book pod found by BeautifulSoup
for page_num in range(1, 41): # Page one through ten
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        # 1. Extract title (its inside <a title="...">)
        title = book.h3.a["title"]

        # Extract price text
        price = book.find("p", class_="price_color").text

        # Extract Availability status
        availability = book.find("p", class_="instock availability").text.strip()

        # Append structured dictionary
        scraped_books.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    print(f"Page {page_num}: {len(books)} books found, running total: {len(scraped_books)}")

# Verify extraction
print(f"Extracted {len(scraped_books)} books successfully")
print(scraped_books[0])

# Create Dataframe
df = pd.DataFrame(scraped_books)

# Inspect raw output
print("\n--- DataFrame Summary ---")
print(df.head())
print("\n--- DataFrame Info ---")
print(df.info())

df["Price"] = df["Price"].str.replace("£", "", regex=False).astype(float)
print(df["Price"].mean())

print(df.info())

print(df["Availability"].value_counts())

df.to_csv("books_cleaned.csv", index=False)
print("Saved!")