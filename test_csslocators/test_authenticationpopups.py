import pytest

from playwright.sync_api import Page, expect,Playwright

@pytest.mark.skip
def test_popups(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(3000)


def test_context_popups(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        http_credentials={"username":"admin","password":"admin"}
    )
    page= context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("div[class='example'] p")).to_be_visible()
    page.wait_for_timeout(3000)



