# B_R_R
# M_S_A_W

import re
from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''
class ParsedItemLocators:
    """
    Locator for an item in the html doc

    This allow us easily see what our code will be looking at
    as well as change quickly if we spot it is different now
    """
    NAME_LOCATOR='article.product_pod h3 a'
    LINK_LOCATOR='article.product_pod h3 a'
    PRICE_LOCATOR='article.product_pod p.price-color'
    RATING_LOCATOR='article.product_pod p.star-rating'


class ParsedItem:
    """
    A class to take in html page and find properties in it
    """
    def __init__(self,page):
        self.soup=BeautifulSoup(page,'html.parser')


    @property
    def name(self):

        locator=ParsedItemLocators.NAME_LOCATOR
        item_link=self.soup.select_one(locator)
        item_name=item_link.attrs['title']
        return (item_name)


    @property
    def link(self):

        locator=ParsedItemLocators.LINK_LOCATOR
        item_link=self.soup.select_one(locator).attrs['href']
        return (item_link)


    @property
    def price(self):

        locator=ParsedItemLocators.PRICE_LOCATOR
        item_price=self.soup.select_one(locator).string #$51.77

        pattern="£([0-9]+\.[0-9]+)"
        matcher=re.search(pattern,item_price)
        #print(matcher.group(0)) #£51.77
        return float(matcher.group(1)) #51.77


    @property
    def rating(self):

        locator=ParsedItemLocators.RATING_LOCATOR
        item_rating=self.soup.select_one(locator)
        classes=item_rating.attrs['class'] # ['star-rating', 'Three']
        rating_class=[r for r in classes if r!='star-rating']
        return rating_class[0]


item=ParsedItem(ITEM_HTML)
print(item.price())
