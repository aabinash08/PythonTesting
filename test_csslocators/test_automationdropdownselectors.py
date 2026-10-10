import pytest

from playwright .sync_api import Page,expect

def test_singledropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # by using the label
    page.locator("#country").select_option("Canada")

    # by using the value
    page.locator("#country").select_option("australia")

    # by using the index value
    page.locator("#country").select_option(index=2)

    #check the number of options in the dropdown
    options = page.locator("#country>option")
    expect(options).to_have_count(10)

    #printing all the text elements
    alloptions= [text.strip() for text in options.all_text_contents()]
    print(alloptions)

    # printing all the options in one after another
    for days in alloptions:
        print(days)
    page.wait_for_timeout(3000)