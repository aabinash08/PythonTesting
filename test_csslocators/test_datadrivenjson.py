import pytest

from playwright .sync_api import Page,expect

import json

files  = open("test_datadrivenfiles/data.json","r")
data_driven  =  json.load(files)



@pytest.mark.parametrize("username, password, validation", [
                         (data["username"],data["password"],data["validation"]) for data in data_driven
])

def test_datadrivenjson(username,password,validation,page:Page):
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