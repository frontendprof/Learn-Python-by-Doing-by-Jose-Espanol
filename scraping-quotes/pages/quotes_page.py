# B_R_R
# M_S_A_W

from bs4 import BeautifulSoup

from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, page):
        self.soup=BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator=QuotesPageLocators.QUOTE
        quote_tags=self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]