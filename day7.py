import requests

url = "https://books.toscrape.com/"
response = requests.get(url)

print(response.encoding)
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