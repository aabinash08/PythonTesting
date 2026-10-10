import pytest
from playwright.sync_api import Page,expect

def test_sortingproducts(page:Page):
    page.goto("https://www.bstackdemo.com/")
    # product=page.locator(".sort")
    # expect(product).to_be_visible()
    # # expect(product).to_be_enabled()


    # page.locator(".sort>select").select_option("Lowest to highest")
    # page.wait_for_timeout(3000)

    prices=page.locator("div>div>div>b")
    prices_products=[text.strip() for text in prices.all_text_contents()]
    print(prices_products)


