import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_pagination(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")
    has_pages=True
    while has_pages:
        all_rows = page.locator("#example tbody tr").all()
        for row in all_rows:
            print(row.inner_text())

    next_button = page.locator("button[class='dt-paging-button next']")
    disabled_button = next_button.get_attribute("class")

    if "disabled" in disabled_button:
        has_pages = False

    else:
        next_button.click()

def test_pagnitaiontables(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")
    dropdown = page.locator("select[aria-controls='example']")
    dropdown.select_option(label='25')
    page.wait_for_timeout(5000)

