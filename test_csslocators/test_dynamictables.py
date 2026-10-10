import pytest

from playwright .sync_api import Page, expect

# def test_dynamictables(page:Page):
#     page.goto("https://practice.expandtesting.com/dynamic-table")
#     table = page.locator("table.table tbody")
#
#     rows = table.locator("tr").all()
#     percentage =""
#     for row in rows:
#       names = row.locator("td").nth(0).inner_text()
#       if names == "Chrome":
#         percentage = row.locator("td:has-text('%')").inner_text()
#         print("CPU of the chrome percentage:", percentage)
#         break
#     page.wait_for_timeout(5000)
#
#     chrome = page.locator("#chrome-cpu")
#     expect(chrome).to_contain_text(percentage)


def test_dynamicautomation(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    all_table = page.locator("table#taskTable tbody")

    rows = all_table.locator("tr").all()
    for row in rows:
        value = row.locator("td").nth(0).inner_text()
        if value =="Chrome":
            cpu = row.locator("td:has-text('%')").inner_text()
            print("CPU load of Chrome process", cpu)
            break



    for row in rows:
        value = row.locator("td").nth(0).inner_text()
        if value =="Firefox":
            memory = row.locator("td:has-text('MB')").inner_text()
            print("Memory Size of Firefox process", memory)
            break
    page.wait_for_timeout(3000)


    for row in rows:
        value = row.locator("td").nth(0).inner_text()
        if value =="Firefox":
            network = row.locator("td:has-text('Mbps')").inner_text()
            print("Network speed of Chrome process:", network)
            break
    page.wait_for_timeout(3000)



    for row in rows:
        value = row.locator("td").nth(0).inner_text()
        if value == "Firefox":
           disk_space  = row.locator("td:has-text('MB/s')").inner_text()
           print("Disk space of  Firefox process", disk_space)
           break
    page.wait_for_timeout(5000)















