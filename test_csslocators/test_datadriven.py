import pytest

from playwright.sync_api import Page,expect

list_of_items = ["laptop","phone","monitor","earphone"]

@pytest.mark.parametrize("item", list_of_items)
def test_datadriven(item,page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(item)
    page.locator("input[type='submit']").click()

    #Assertion
    verify = page.locator("h2 a").nth(0)
    expect(verify).to_contain_text(item,ignore_case=True)

