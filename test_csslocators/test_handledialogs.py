import pytest

from playwright.sync_api import Page, expect

def test_handledialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Approach2
    page.on("dialog", lambda dialog:dialog.accept('Abinash'))

    # page.on("dialog", lambda dialog:dialog.dismiss())
    page.wait_for_timeout(5000)

    # page.locator("#alertBtn").click()
    # page.locator("#confirmBtn").click()
    page.locator("#promptBtn").click()
    # page.wait_for_timeout(3000)

    result1 = page.locator("#demo").inner_text()
    print(result1)

    expect(page.locator("#demo")).to_have_text("Hello Abinash! How are you today?")
    page.wait_for_timeout(3000)

