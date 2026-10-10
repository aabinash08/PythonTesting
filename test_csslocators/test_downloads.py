import pytest

from playwright.async_api import Page, expect

def test_dowloadpage(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("Welcome")
    page.locator("#generateTxt").click()

    page.on("download", lambda download: download.save_as("downloads/testfile.txt"))

    page.locator("#txtDownloadLink").click()
    page.wait_for_timeout(5000)