import pytest

from playwright .sync_api import Page,expect

def test_inputbuttons(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#name").fill("Abinash")
    page.wait_for_timeout(2000)

    #visibility of the element
    input =page.locator("#name")
    expect(input).to_be_visible()
    expect(input).to_be_enabled()

    #Check the attribute element
    expect(input).to_have_attribute("maxlength","15")

    #get the attribute of an element
    value = input.get_attribute("maxlength")
    print(value)

    #fill the names/ and get the input value
    input.fill("Ramesh")
    name = input.input_value()
    page.wait_for_timeout(2000)
    print(name)

def test_radiobutton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    checkbox = page.locator("#male")

    #visibility and enabled of the element
    expect(checkbox).to_be_visible()
    expect(checkbox).to_be_enabled()
    page.wait_for_timeout(1000)

    #selecting the checkbox
    checkbox.check()
    expect(checkbox).to_be_checked()

    page.goto("https://testautomationpractice.blogspot.com/")
    checkbox = page.locator("#male")
    page.wait_for_timeout(1000)

    #Unselecting the Checkbox
    checkbox.uncheck()
    expect(checkbox).not_to_be_checked()


def test_checkboxbuttons(page:Page):

    #specfically selecting the checkbox
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.locator("#sunday").check()
    # page.wait_for_timeout(1000)

    #selecting all the element in the checkboxes
    data = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    checkboxes=[page.get_by_label(day) for day in data]

    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()
    page.wait_for_timeout(3000)


    # need all the elements to be unchecked
    for checkbox in checkboxes:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
    page.wait_for_timeout(3000)

   # Checking the last 3 elements
    for checkbox in checkboxes[-3:]:
        checkbox.check()
    page.wait_for_timeout(3000)

    # Toggle the checkbox elements
    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()
    page.wait_for_timeout(3000)

    # Checking the element based on the index value
    index=[1,3,6]
    for i in index:
        checkboxes[i].check()
        expect(checkboxes[i]).to_be_checked()
    page.wait_for_timeout(3000)

    # checking the element by using the label
    day="Friday"
    specific = page.get_by_label(day)
    specific.check()
    expect(specific).to_be_checked()
    page.wait_for_timeout(1000)
    #
    # Another Method
    weekday ="Friday"
    for day in data:
        if day==weekday:
          Days = page.get_by_label(day)
          Days.check()
          expect(Days).to_be_checked()
    page.wait_for_timeout(2000)




















