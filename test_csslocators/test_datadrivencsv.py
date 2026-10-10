
import pytest

from playwright.sync_api import Page,expect

import csv


login_data=[]

file=open("test_datadrivenfiles/data.csv",newline='',encoding='utf-8')
reader = csv.DictReader(file)
for row in reader:
    login_data.append((row["username"],row["password"],row["validation"]))

@pytest.mark.parametrize("username,password,validation",login_data)
def test_datadrivencsv(username,password,validation,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("#Email").fill(username)
    page.locator("#Password").fill(password)
    page.locator("input[value='Log in']").click()


    #Assertion

    if  validation=="valid":
        logout = page.locator(".ico-logout")
        expect(logout).to_be_visible(timeout=5000)
    else:
      error_message = page.locator(".validation-summary-errors")
      expect(error_message).to_be_visible(timeout=5000)
      expect(page).to_have_url("https://demowebshop.tricentis.com/login")