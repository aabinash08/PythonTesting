import pytest
from playwright .sync_api import Page, expect

def test_radiobutton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_button=page.locator("#male")

    # to check the visibility of the element and enabled or not
    expect(male_button).to_be_visible()
    expect(male_button).to_be_enabled()

    # verify the radio buttons not to be checked
    expect(male_button).not_to_be_checked()

    # # fill the options in check mode
    male_button.click()

    #verify the radio buttons to be checked
    expect(male_button).to_be_checked()
    page.wait_for_timeout(2000)



    #verify how many checkboxes
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    checkboxes=[page.get_by_label(day)for day in days]
    print("Total number of checkbox:", len(checkboxes))

    #selecting the checkboxes

    # for checkbox in checkboxes:
    checkboxes.check()
    expect(checkboxes).to_be_checked()
    page.wait_for_timeout(2000)


    #verifying the selected checkboxes
    for checkbox in checkboxes[-3:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
        page.wait_for_timeout(2000)



    # verify the selected checkbox to be unchecked and unchecked to selected
    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()
            page.wait_for_timeout(2000)


     # Randomly selecting the checkboxes like 1,3 and 6
      indexes=[1,3,6]
    for i in indexes:
        checkboxes[i].check()
        expect(checkboxes[i]).to_be_checked()
    page.wait_for_timeout(6000)

    weekday= "Thursday"
    for label in days:
        if label == weekday:
            checkboxes=page.get_by_label(label)
            checkboxes.check()
            expect(checkboxes).to_be_checked()
    page.wait_for_timeout(3000)










