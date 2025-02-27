from bs4 import BeautifulSoup as bs
import requests

URL = "https://books.toscrape.com/?form=MG0AV3"
page = requests.get(URL)
soup = bs(page.content, "html.parser")
page_number = 1

while page_number <= 50:
    # Find all the title of the books
    result = soup.find_all("a", {'title': True})

    for title in result:
        book_title = title.get('title')
        if book_title:
            print(f'Book Title: {book_title}')

    print(f"page {page_number} completed")
    page_number += 1
    URL = f"https://books.toscrape.com/catalogue/page-{page_number}.html"