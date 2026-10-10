import pytest
from playwright.sync_api import Page,expect

# page.get_by_alt_text
# page.get_by_text
# page.get_by_role
def test_playwrightlocators(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_alt_text("logo image")).to_be_visible()


    expect(page.get_by_text("This paragraph contains some ")).to_be_visible()
    expect(page.get_by_text("List item 2 with ")).to_be_visible()


    expect(page.get_by_role("heading", name="PlaywrightPractice")).to_be_visible()


    page.get_by_label("Email Address:").fill("aabinash08@gmail.com")
    page.get_by_label("Password:").fill("Blueblack@123")


    page.get_by_placeholder("Enter your full name").fill("Abinash")

    expect(page.get_by_title("Home page link")).to_have_text("Home")

    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
