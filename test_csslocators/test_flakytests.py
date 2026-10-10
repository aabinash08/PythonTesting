import pytest

from playwright.sync_api import Page,expect

def test_flakytests(page:Page):
    page.goto("https://demoblaze.com/index.html")
    page.wait_for_timeout(5000)
    page.locator("#login2").click()
    username = page.locator("#loginusername").fill("pavnol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button[onclick='logIn()']").click()
    page.wait_for_timeout(3000)
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavnol")

