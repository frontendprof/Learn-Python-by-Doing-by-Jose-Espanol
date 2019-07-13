# B_R_R
# M_S_A_W

from locators.quote_locators import QuoteLocators

class QuoteParser:
    """
    Given one specific quote divs, find out the data about
    the quote(author, content, tag)

    """
    def __init__(self, parent):
        self.parent=parent


    def __repr__(self):
        return f"<Quote {self.content}, by {self.author}>"

    @property
    def content(self):
        locator=QuoteLocators.CONTENT
        return self.parent.select_one(locator).string


    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tag(self):
        locator = QuoteLocators.TAG
        return [t.sting for t in self.parent.select(locator)] # Not selects just one, but selects all and extracts then
