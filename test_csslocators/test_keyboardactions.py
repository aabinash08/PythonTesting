import pytest

from playwright.sync_api import Page,expect

def test_keyboard(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    input1 = page.locator("#input1")

    #Focus
    input1.focus()

    #Provide the text in the input1
    page.keyboard.insert_text("Welcome")

    #Selecting the item
    page.keyboard.press("Control+A")

    #Copying the item
    page.keyboard.press("Control+C")

    #switching to Another input box
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #Again copying the same item
    page.keyboard.press("Control+V")

    #Now again Tab switch
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #Again copying the same item
    page.keyboard.press("Control+V")

    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    expect(input2).to_have_value("Welcome")
    expect(input2).to_have_value("Welcome")






