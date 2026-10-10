import pytest

from playwright.sync_api import Page,expect

def test_newwebsite(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect (page.get_by_alt_text("Tricentis Demo Web Shop")).to_be_visible()
    page.wait_for_timeout(3000)
    page.locator("a[href*='computer']")
    page.wait_for_timeout(3000)
    page.goto("https://demowebshop.tricentis.com/")
    print(expect(page.get_by_text("$25 Virtual Gift Card")).to_be_visible())
    print(expect(page.get_by_text("Simple Computer")).to_be_visible())
    page.wait_for_timeout(3000)


