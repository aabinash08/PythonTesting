import pytest


from playwright.sync_api import  Page , expect

class Homepage:
    def __init__(self, page:Page):
        self.page = page
        #css selector targetting all the elements
        self.all_products = "h4 .hrefch"

        #Add to cart button (exact match using the text)
        self.add_to_product_button = page.locator("div [class='btn btn-success btn-lg']")

        #cart button in the top menu
        self.cart_button= page.locator("#cartur")

    def add_products_to_the_cart(self,product_name):
        products = self.page.locator(self.all_products)
        count         =  products.count()

        for i in range(count):
            name = products.nth(i).text_content().strip()
            if name == product_name:
                products.nth(i).click()
                break

        self.page.on("dialog", lambda dialog : dialog.accept())
        self.add_to_product_button.click()

    def go_to_cart(self):
        self.cart_button.click()

