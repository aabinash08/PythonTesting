import pytest

from playwright.sync_api import Page,expect

def test_sample(page:Page):
    page.goto("https://demoblaze.com")
    expect(page.locator(".hrefch").filter(has_text="Samsung galaxy s6")).to_be_visible()
    page.wait_for_timeout(3000)


def test_sample2(page:Page):
    page.goto("https://demoblaze.com/index.html")
    page.locator("#login2").click()
    page.wait_for_timeout(3000)
    page.locator("#loginusername").fill("pavnol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button[onclick='logIn()']").click()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavnol")

def test_sample3(page:Page):
    page.goto("https://demoblaze.com")
    expect(page.locator(".hrefch").filter(has_text="Iphone 6 32gb")).to_be_visible()
    page.wait_for_timeout(2000)




