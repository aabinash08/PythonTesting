import pytest
from playwright.sync_api import Page, expect

def test_page(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.locator("img[alt='Tricentis Demo Web Shop']")).to_be_visible()
    products = page.locator("h2>a[href*='mpu']")
    expect(products).to_have_count(4)
    computer_products = page.locator("h2>a").all_text_contents()
    print(computer_products)
    fb = page.locator("li[class='facebook']")
    print(fb)
    page.wait_for_timeout(2000)

