import pytest

from playwright.sync_api import Page, expect,Playwright

def test_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page1= context.new_page()
    page2=context.new_page()

    page1.goto("https://www.google.com/")
    page1.wait_for_timeout(3000)

    page2.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page2.wait_for_timeout(3000)







