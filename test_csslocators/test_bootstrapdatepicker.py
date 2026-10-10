import pytest

from playwright.sync_api import Page,expect

def check_in_date(page,month,year,date):
    while True:
        check_in_month = page.locator("h3[aria-live='polite']").nth(0).inner_text()
        Month, Year = check_in_month.split(" ")
        if Month == month and Year == year:
            break
        else:
            page.locator('button[aria-label="Next month"]').click()

    all_Dates = page.locator("table.b8fcb0c66a tbody").nth(0).locator("td").all()

    for Date in all_Dates:
        if Date.inner_text() == date:
            Date.click()
            break
        else:
            break

def check_out_date(page,month,year,date):
    while True:
        check_in_month = page.locator("h3[aria-live='polite']").nth(1).inner_text()
        Month, Year = check_in_month.split(" ")
        if Month == month and Year == year:
            break
        else:
            page.locator('button[aria-label="Next month"]').click()

    all_Dates = page.locator("table.b8fcb0c66a tbody").nth(1).locator("td").all()

    for Date in all_Dates:
        if Date.inner_text() == date:
            Date.click()
            break


def test_bootstrapdatepicker(page:Page):
    page.goto("https://www.booking.com/")
    close_button = page.locator("button[aria-label='Dismiss']")

    if close_button.is_visible():
        close_button.click()

    selector = page.get_by_test_id("searchbox-dates-container")
    selector.click()
    check_in_date(page,"September","2026","22")
    check_out_date(page,"October","2026","7")

    checkin_month = page.locator("#bui-calendar-month-2026-8").inner_text()
    checkout_month = page.locator("#bui-calendar-month-2026-9").inner_text()

    print("checkin_month:",checkin_month)
    print("checkout_month:",checkout_month)

    expect(selector).to_contain_text(checkin_month)
    expect(selector).to_contain_text(checkout_month)






