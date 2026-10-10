import pytest

from playwright.sync_api import Page, expect,Playwright

def test_handlepopups(playwright: Playwright):
   browser = playwright.chromium.launch(headless=False)
   context = browser.new_context()
   page = context.new_page()

   page.goto("https://testautomationpractice.blogspot.com/")

   page.on("popup", lambda popup:popup.wait_for_load_state())

   page.locator("#PopUp").click()
   page.wait_for_timeout(3000)

   all_popups = context.pages
   print("Total no.ofpages",len(all_popups))

   for popup in all_popups:
       print(popup.url)
       title = popup.title()
       if "Playwright" in title:
           popup.locator(".getStarted_Sjon").click()
           popup.close()
           page.wait_for_timeout(3000)
       # if "Selenium" in title:
       #     popup.locator(".getStarted_Sjon").click()
       #     popup.close()

   context.close()
   browser.close()





