import pytest

from playwright.sync_api import Playwright,Page,expect

def test_videorecorder(playwright: Playwright):
   browser =  playwright.chromium.launch(headless=False)
   context= browser.new_context()
   context.tracing.start(screenshots=True,snapshots=True)
   page = context.new_page()
   page.goto("https://demoblaze.com/index.html")
   page.locator("#login2").click()
   page.locator("#loginusername").fill("pavnol")
   page.locator("#loginpassword").fill("test@123")
   page.locator("button[onclick='logIn()']").click()
   page.wait_for_timeout(3000)

   #Stopping the trace
   context.tracing.stop(path="trac.zip")
   context.close()
   browser.close()


