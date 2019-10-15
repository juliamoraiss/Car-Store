import pymysql
from time import sleep
from modules import insert, menu, exit_menu, update, delete_row

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="lab_mysql2"
)
c = db.cursor()

while True:
    menu("Choose a table: ", "Cars", "Customers", "Invoices", "Manufacturer", "Salesperson", "Store", "Exit")
    option1 = int(input('\n\033[32mOption: \033[m'))
    sleep(0.5)

    if option1 == 7:
        exit_menu()

    menu("Choose an option: ", "Insert new record", "Update record", "Delete row", "Exit")
    option2 = int(input('\n\033[32mOption: \033[m'))
    sleep(0.5)

    if option2 == 4:
        exit_menu()

    if option1 == 1:
        col = 'cars'
        if option2 == 1:
            insert(col)
        if option2 == 2:
            update(col)
        if option2 == 3:
            delete_row(col)

    if option1 == 2:
        col = 'customers'
        if option2 == 1:
            insert(col)
        if option2 == 2:
            update(col)
        if option2 == 3:
            delete_row(col)

    if option1 == 3:
        col = 'invoices'
        if option2 == 1:
            insert(col)
        if option2 == 2:
            update(col)
        if option2 == 3:
            delete_row(col)

    if option1 == 4:
        col = 'manufacturer'
        if option2 == 1:
            insert(col)
        if option2 == 2:
            update(col)
        if option2 == 3:
            delete_row(col)

    if option1 == 5:
        col = 'salesperson'
        if option2 == 1:
            insert(col)
        if option2 == 2:
            update(col)
        if option2 == 3:
            delete_row(col)

    if option1 == 6:
        col = 'store'
        if option2 == 1:
            insert(col)
        if option2 == 2:
            update(col)
        if option2 == 3:
            delete_row(col)

    option3 = str(input('Return to menu? [Y/N]: ')).upper().strip()

    if option3 == 'N':
        break