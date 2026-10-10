import pytest

from playwright.sync_api import Page, expect,Playwright

def test_tabs(playwright:Playwright):
   browser = playwright.chromium.launch(headless=False)
   context = browser.new_context()
   parentpage = context.new_page()

   parentpage.goto("https://testautomationpractice.blogspot.com/")
   parentpage.on("page",lambda page:page.wait_for_load_state())

   parentpage.locator("button[onclick='myFunction()']").click()
   parentpage.wait_for_timeout(5000
                               )
   all_pages = context.pages
   print("Total no.of tabs",len(all_pages))
   print("Title of parent page",all_pages[0].title())
   print("Title of child page",all_pages[1].title())

   childpage=all_pages[1]
   print("Child page of the url", childpage.url)



