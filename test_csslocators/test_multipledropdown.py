import pytest
from playwright.sync_api import Page,expect

def test_colorsdropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.locator("#colors").select_option(["Red","Green","White"]) #by label
    # page.wait_for_timeout(6000)

    # page.locator("#colors").select_option(value=["Red", "Green", "White"])  # by value
    # page.wait_for_timeout(3000)

    # drop_down=page.locator("#colors>option")   #to have the count
    # expect(drop_down).to_have_count(7)

    # drop_down=page.locator("#colors>option")
    # Dropdown=[text.strip() for text in drop_down.all_text_contents()] #printing all the dropdown texts
    # print(Dropdown)

    drop_down = page.locator("#colors>option")
    Dropdown = [text.strip() for text in drop_down.all_text_contents()]
    options=Dropdown.copy()
    Option=sorted(Dropdown)
    print("Original List:",options)
    print("Sorted List",Option)


    











