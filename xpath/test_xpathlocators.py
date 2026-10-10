import pytest
from playwright.sync_api import Page,expect

def test_xpathlocators(page:Page): #full x-path
    page.goto("https://demowebshop.tricentis.com/")
    logo=page.locator("//html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
    expect(logo).to_be_visible()

    logo=page.locator("//img[@alt='Tricentis Demo Web Shop']") #relative x-path - syntax: //tagname[@attribute='name']
    expect(logo).to_be_visible()
    page.wait_for_timeout(5000)

    product=page.locator("//h2//a[contains(@href,'computer')]")   #contains concept
    print("The Product count",product.count())
    expect(product).to_have_count(4)                              #count concept
    print("First Product:", product.first.text_content())         #first_element
    print("Last Product:", product.last.text_content())           #last_elemet
    print("N-th Product:", product.nth(2).text_content())         #nth_element


    start_products=page.locator("//h2//a[starts-with(@href, '/build')]")   #starts-with function concept
    product_start=start_products.count()
    print("Count of the Building Products:",product_start)
    expect(start_products).to_have_count(product_start)

    link_register=page.locator("//a[text()='Register']")  #inner text concept
    expect(link_register).to_be_visible()

    Google_locator=page.locator("//div[@class='column follow-us']//li[last()]")           #specifically taking the last element
    expect(Google_locator).to_be_visible()

    Position_0f_google=page.locator("//div[@class='column follow-us']//li[position()=5]")   #position of the element and print
    expect(Position_0f_google).to_have_text("Google+")















