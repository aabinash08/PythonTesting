import pytest


from playwright.sync_api import  Page , expect

class Loginpage:

    def __init__(self,page:Page):
        self.page=page
        self.login_page=self.page.locator("#login2")
        self.username=self.page.locator("#loginusername")
        self.password=self.page.locator("#loginpassword")
        self.login_button=self.page.locator("button[onclick='logIn()']")

    #Action methods
    def click_login_link(self):
        self.login_page.click()

    def fillusername(self,username):
        self.username.fill("")     #clears the input box
        self.username.fill(username)

    def fillpassword(self,password):
        self.password.fill("")
        self.password.fill(password)

    def click_login_button(self):
        self.login_button.click()




