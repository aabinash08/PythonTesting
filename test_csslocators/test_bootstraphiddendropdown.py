import pytest

from playwright .sync_api import Page,expect

def test_bootstraphidden(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(2000)


    page.get_by_text("PIM").click()
    page.wait_for_timeout(1000)

    # selecting the dropdown
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(1000)


    #No. of Counts
    products = page.locator("div[role='listbox']>div span")
    totalcount = products.count()
    print("Total no. of the products:",totalcount)
    expect(products).to_have_count(totalcount)
    page.wait_for_timeout(5000)

    #Printing specifically the text element
    print(products.nth(2).text_content())
    page.wait_for_timeout(1000)

    #Printing all the elements

    for i in range(totalcount):
      all_products = products.nth(i).text_content()
      print(all_products)

    checkbox=[j.strip() for j in products.all_text_contents()]
    print(checkbox)


    selectoption="Chief Executive Officer"
    for i in range(totalcount):
      select = products.nth(i).text_content()
      if select ==selectoption:
          products.nth(i).click()
          break
    page.wait_for_timeout(2000)






















