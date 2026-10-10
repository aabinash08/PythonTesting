import pytest


from playwright.sync_api import  Page , expect


class Cartpage:
    def __init__(self, page:Page):
        self.page = page
        self.cart_page = "tbody tr td:nth-child(2)"

    def cart_page_action(self,product_name):
        products = self.page.locator(self.cart_page)
        count = products.count()

        for i in range(count):
            name  =  products.nth(i).text_content().strip()
            if name==product_name:
                return products.nth(i)

        return None

