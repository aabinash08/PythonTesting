import pytest

from playwright.sync_api import Page,expect

login_testdata =[ ("laura.taylor1234@example.com","test123","valid"),
                  ("aabinash08@gmail.com","Blueblack@321","invalid"),
                  ("","","invalid")
]
@pytest.mark.parametrize("username,password,validation",login_testdata)
def test_datadriven_1(username,password,validation,page:Page):
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