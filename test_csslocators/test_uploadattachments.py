import pytest

from playwright.sync_api import Page,expect


@pytest.mark.skip
def test_uploaddocuments(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#singleFileInput").set_input_files("upload\download.jpg")
    page.locator("button:has-text('Upload Single File')").click()
    page.wait_for_timeout(5000)


#multiple attachements 
def test_uploadattachments(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    files=["upload\download.jpg","upload\oggy.jpg"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple Files')").click()
    page.wait_for_timeout(5000)


    #validation
    status1 = page.locator("#singleFileStatus")
    expect(status1).to_contain_text("download.jpg")


