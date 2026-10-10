import pytest
from playwright.sync_api import Page,expect

def select_date(page,target_date,target_month,target_year, is_future):
    while True:
        current_month = page.locator(".ui-datepicker-month").text_content()
        current_year = page.locator(".ui-datepicker-year").text_content()

        if current_month == target_month and current_year == target_year:
            break
        if is_future == True:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    total_dates = page.locator("#ui-datepicker-div td").all()
    for all in total_dates:
        all_dates = all.inner_text()
        if all_dates == target_date:
            all.click()
            break



def test_jquerydate(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Appraoch01
    date_element = page.locator("#datepicker")
    # date_element.fill("12/06/2001")
    # page.wait_for_timeout(2000)
    # expect(date_element).to_have_value("12/06/2001")

    #Appraoch 02
    is_future = True
    year = "2001"
    date= "6"
    month="December"
    date_element.click()
    select_date(page,date,month,year,is_future)


