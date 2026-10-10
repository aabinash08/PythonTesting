import pytest

from playwright .sync_api import Page,expect

def test_multipledropdownselector(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #by using the label:
    # page.locator("#colors").select_option(value=["Red","Green","White"])
    # page.wait_for_timeout(5000)

    #by using the value :
    # page.locator("#colors").select_option(value=["blue","yellow","green"])
    # page.wait_for_timeout(5000)

    #by using the index value
    # page.locator("#colors").select_option(index=[0,2,4])
    # page.wait_for_timeout(5000)

    # how many elements by using the assertion
    # count = page.locator("#colors>option")
    # expect(count).to_have_count(7)
    # page.wait_for_timeout(3000)

    #Printing all the text elements
    # all_values = page.locator("#colors>option")
    # all_elements =[text.strip() for text in all_values.all_text_contents()]
    # print(all_elements)
    # for i in all_elements:
    #     print(i)
    # page.wait_for_timeout(3000)

    #Sorting the value
    all_values = page.locator("#colors>option")
    # all_values = page.locator("#animals>option")
    all_elements = [text.strip() for text in all_values.all_text_contents()]
    original_list = all_elements.copy()
    sorted_list = sorted(all_elements)
    print(original_list)
    print(sorted_list)
    page.wait_for_timeout(3000)

    if original_list==sorted_list:
        print("It is sorted correctly")
    else:
        print("It is NOT sorted correctly")











