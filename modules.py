import MySQLdb
from time import sleep

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    database="lab_mysql2"
)
c = db.cursor()


def exit_menu():
    print('-' * 40)
    print(f'{"SEE YOU LATER! :)":^40}')
    print('-' * 40)
    exit()


def menu(title, *option):
    print('\033[31m=' * 40)
    print(f'{title:^40}')
    print('=' * 40)
    print('\033[m')
    cont = 1
    for n in option:
        print(f'\033[33m{cont} -\033[m\033[34m {n}')
        cont += 1


def list_table(table):
    c.execute(f'SELECT * from {table}')
    records = c.fetchall()
    for r in records:
        print(r)


def show_columns(table):
    columns = list()
    c.execute(f'DESC {table}')
    desc = c.fetchall()
    for column in desc:
        columns.append(column[0])
    return ", ".join(columns[1:])


def insert(table):
    print('-' * 40)
    print(f'{"INSERT NEW RECORD":^40}')
    print('-' * 40)
    columns = show_columns(table)
    columns_list = columns.split(', ')
    columns_list_lenght = len(columns_list)
    symbol_values = columns_list_lenght * '%s, '
    cont = 0
    op = 'Y'
    while op == 'Y':
        query = f"insert into {table} ({columns}) values ({symbol_values[:-2]})"
        values = list()
        for col_name in columns_list:
            if col_name[0:2] == 'id':
                list_table(col_name[3:])
            values.append(input(f"{col_name}: "))
        c.execute(query, values)
        db.commit()
        sleep(0.5)
        op = input("Add another record? [Y/N]: ").upper().strip()
        sleep(0.5)
        cont += 1
    print(f"\nDONE! {cont} record(s) inserted.\n")


def update(col):
    print('-' * 40)
    print(f'{"UPDATE RECORD":^40}')
    print('-' * 40)
    op = "Y"
    cont = 0
    while op == 'Y':
        column = str(input('Column: ').lower())
        update = str(input('Update to: '))
        id = int(input('id_cars: '))
        query = f"update cars set {column} = '{update}' where id_{col} = {id}"
        c.execute(query)
        db.commit()
        op = input("Update another record? [Y/N]: ").upper().strip()
        cont += 1
    print(f"\nDONE! {cont} record(s) updated.\n")


def delete_row(col):
    print('-' * 40)
    print(f'{"DELETE ROW":^40}')
    print('-' * 40)
    op = "Y"
    cont = 0
    while op == 'Y':
        id = int(input(f'id_{col}: '))
        query = f"delete from cars where id_{col} = {id}"
        c.execute(query)
        db.commit()
        op = input("Delete another row? [Y/N]: ").upper().strip()
        cont += 1
    print(f"\nDONE! {cont} row(s) deleted.\n")

