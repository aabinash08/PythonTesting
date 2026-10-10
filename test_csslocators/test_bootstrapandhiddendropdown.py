import pytest
from playwright.sync_api import Page,expect

def test_bootstrapandhiddendropdown(page:Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")




    #Logging the Webpage
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[type='password']").fill("admin123")
    page.locator("button[type='submit'] ").click()
    page.wait_for_timeout(3000)

    #selecting the PIM Option
    page.get_by_text("PIM").click()

    #selecting the Job Title Section
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(3000)


    # Taking all the elements in the Job Title section
    options=page.locator("div[role='listbox'] span")
    count=options.count()
    print("Number of options:", count)
    page.wait_for_timeout(3000)

    #Printing all the elements from the Job Title Section
    print(options.all_text_contents())

    #Priting all the elements in one after another
    for i in range(count):
        print(options.nth(i).text_content())


    #selecting or clicking the option
    for i in range(count):
        select=options.nth(i).text_content()
        if select=="Automaton Tester":
            print("Option is selected:", select)
            print("Matching is Successful")
            options.nth(i).click()
            break
    page.wait_for_timeout(5000)









