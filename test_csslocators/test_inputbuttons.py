import pytest
from playwright .sync_api import Page, expect

def test_inputboxes(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_box=page.locator("#name")

    # to check the visibility of the element and enabled or not
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    #check the attribute of an element
    expect(text_box).to_have_attribute("maxlength","15")

    #get an attribute
    Maxlength=text_box.get_attribute("maxlength")
    print("Max Length is", Maxlength)

    #fill the text or the input value
    text_box.fill("Abinash")

    #show the text of the input value
    inputs=text_box.input_value()
    print("The input is", inputs)
    page.wait_for_timeout(10000)


