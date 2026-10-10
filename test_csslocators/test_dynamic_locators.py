import pytest
from playwright.sync_api import Page,expect

def test_dynamic_locator(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//button[contains(@name,'st')] ")

    for i in range(5):
        buttons = page.locator("//button[contains(@name,'st')]")
        buttons.click()
        page.wait_for_timeout(5000)





