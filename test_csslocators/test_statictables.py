import pytest

from playwright .sync_api import Page, expect

def test_static_tables(page:Page):
    #locating the table
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    #counting the Table Values
    table_rows = table.locator("tr")
    page.wait_for_timeout(5000)
    expect(table_rows).to_have_count(7)

    #Taking the total number of counts in the table
    table_count = table_rows.count()
    print("Total Number of Table Rows: ",table_count)  #7
    page.wait_for_timeout(2000)

    #Taking only the column/header in the table
    table_columns = table_rows.locator("th")
    column_table = table_columns.count()
    print("Total Number of Table Columns: ",column_table)  #4
    page.wait_for_timeout(2000)


    #specifically taking any rows:
    specific_rows = table_rows.nth(4).locator("td")
    specific_texts =specific_rows.all_inner_texts()
    print(specific_texts)
    for text in specific_texts:
        print(text)
    page.wait_for_timeout(5000)

    #Taking all the rows excluding the column/header
    total_rows = table_rows.all()
    for rows in total_rows[1:]:
      all_rows = rows.locator("td").all_inner_texts()
      print(all_rows)

    #Printing the book names based on the author

    for rows in total_rows[1:]:
        author_name = rows.locator("td").nth(1).inner_text()
        if author_name == 'Mukesh':
         book_name  = rows.locator("td").nth(0).inner_text()
         print(f"{book_name} /t { author_name}")
    page.wait_for_timeout(5000)













