import pytest
from playwright.sync_api import Page,expect


from loginpage import Loginpage
from homepage import Homepage
from cartpage import Cartpage

@pytest.mark.parametrize("username,password,product_name",[
    ("pavnol","test@123","Samsung galaxy s6")
])

def test_user_login_add_product_to_cart(page:Page,username,password,product_name):
    page.goto("https://demoblaze.com/index.html")

    #login actions
    login_page = Loginpage(page)
    login_page.click_login_link()
    login_page.fillusername(username)
    login_page.fillpassword(password)
    login_page.click_login_button()

    #Home page actions
    home_page = Homepage(page)
    home_page.add_products_to_the_cart(product_name)
    page.wait_for_timeout(5000)
    home_page.go_to_cart()
    page.wait_for_timeout(5000)


    #cart actions
    cart_page  = Cartpage(page)
    product_in_cart = cart_page.cart_page_action(product_name)

    #validation
    expect(product_in_cart).to_be_visible()









