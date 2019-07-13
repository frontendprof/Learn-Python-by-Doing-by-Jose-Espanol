# B_R_R
# M_S_A_W

import requests
from pages.quotes_page import QuotesPage

page_content=requests.get('http://quotes.toscrape.com').content
page=QuotesPage(page_content)

for quote in page.quotes:
    print(quote)
