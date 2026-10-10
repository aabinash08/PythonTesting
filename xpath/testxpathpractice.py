import pytest

from playwright .sync_api import Page,expect

def test_xpathpractice(page:Page):
    #Relative X path
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.locator("//img [@alt='Tricentis Demo Web Shop']")).to_be_visible()

    #x-path with contains
    prodcuts= page.locator("//h2//a [contains(@href,'computer')]")
    computer = prodcuts.count()
    print("No.of Computer Products:", computer)
    expect(prodcuts).to_have_count(4)
    page.wait_for_timeout(2000)
    print("First_Product", prodcuts.first.text_content())
    print("Last Product", prodcuts.last.text_content())
    print("Nth Products", prodcuts.nth(0).text_content())

    all_products = prodcuts.all_text_contents()
    print("All_Products", all_products)

    for i in all_products:
        print(i)

    #starts-with()
    build = page.locator("//h2//a [starts-with(@href,'/build')]")
    build_products = build.count()
    print("No.of Build Products:", build_products)
    expect(build).to_have_count(build_products)

    #text()
    expect(page.locator("//li//a[text()='Register']")).to_be_visible()

    #last()
    website =page.locator("//div[@class='column follow-us']//li[last()]")
    page.wait_for_timeout(2000)
    print(website.text_content())

    #position()
    another = page.locator("//div[@class='column follow-us']//li[position()=4]")
    print(another.text_content())

    #Dynamic element
    page.goto("https://testautomationpractice.blogspot.com/")


    for i in range(5):
        dynamic = page.locator("//button[starts-with(@name,'st')]")
        dynamic.click()
        page.wait_for_timeout(5000)













