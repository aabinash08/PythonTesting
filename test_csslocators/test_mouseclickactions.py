import pytest

from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_mouseactionshover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    click = page.locator(".dropbtn")
    click.hover()

    options = page.locator(".dropdown-content a:nth-child(2)")
    options.hover()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouseactionsdoubleclick(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    double_click = page.locator("button[ondblclick='myFunction1()']")
    double_click.dblclick()

    field2 =page.locator("#field2")
    expect(field2).to_have_value("Hello World!")

    page.wait_for_timeout(3000)



@pytest.mark.skip
def test_mouseactionsdragdrop(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    source = page.locator("#draggable")
    target = page.locator("#droppable")

    source.drag_to(target)
    page.wait_for_timeout(5000)


def test_rightclick(page: Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    right_click = page.locator(".context-menu-one")
    right_click.click(button="right")
    page.wait_for_timeout(5000)





