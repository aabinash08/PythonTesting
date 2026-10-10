import pytest
from playwright.sync_api import Page,expect

def test_singledropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #verify using the dropdown with get by label
    # page.locator("#country").select_option("Germany") #label option is Germany
    # page.wait_for_timeout(3000)

    #by verify using the value
    # page.locator("#country").select_option("india")
    # page.locator("#country").select_option(value="India")  #get by the value
    # page.wait_for_timeout(3000)

    #By verifying with the indexes
    # page.locator("#country").select_option(index = 2)  #get by the index
    # page.wait_for_timeout(3000)

    #how many number of options in the dropdowns:
    dropdown=page.locator("#country>option")
    expect(dropdown).to_have_count(10)
    listoption=[text.strip() for text in dropdown.all_text_contents()]
    print(listoption)

    #to show in the Next line options
    for n in listoption:
        print(n)







