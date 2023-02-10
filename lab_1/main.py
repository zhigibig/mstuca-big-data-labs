import pandas as pd
import data_generators as gen 
import sqlite3
from addresses_of_files import excel_table_adress, sql_database_adress
from sqlalchemy import create_engine

def data_exporting(data):
    data.to_excel(excel_table_adress)

    conn = sqlite3.connect('Customer_base')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS products (fname text, sname text, lname text, date text, session_time text, day_time text, film text, genre text, hall number, row number, seat number, price number)')
    conn.commit()

    data.to_sql('Customer_base', conn, if_exists='replace', index = False)
 
    c.execute('SELECT * FROM Customer_base')

    for r in c.fetchall():
        print (r)
    
    data.to_csv('Table in CSV type', sep='\t', encoding='utf-8')

    return 0


def table_creation(number_of_lines):
    columns = [
                'First Name', 'Middle Name', 'Last Name', 'Date', "Session's time", "Day time",
                "Film", "Genre", 'Hall', "Row", "Seat", "Ticket's Price",
              ]

    table = {}

    for i in columns:
        table[f'{i}'] = []
    
    for i in range(number_of_lines):
        instance = [
            gen.clients_fname(), gen.c_mname(), gen.c_lname(), 
            gen.random_date(), gen.sessions_time(), gen.day_time(), 
            gen.film(), gen.genre(), gen.hall_num(), 
            gen.row(), gen.seat(), gen.pricing(),
        ]

        for e in range(len(columns)):
            table[columns[e]].append(instance[e])
    
    return table

def main():
    NUMBER_OF_LINES = 137_822

    columns = [
                'First Name', 'Middle Name', 'Last Name', 'Date', "Session's time", "Day time",
                "Film", "Genre", 'Hall', "Row", "Seat", "Ticket's Price",
              ]

    table = {}

    for i in columns:
        table[f'{i}'] = []
    
    for i in range(NUMBER_OF_LINES):
        instance = [
            gen.clients_fname(), gen.c_mname(), gen.c_lname(), 
            gen.random_date(), gen.sessions_time(), gen.day_time(), 
            gen.film(), gen.genre(), gen.hall_num(), 
            gen.row(), gen.seat(), gen.pricing(),
        ]

        for e in range(len(columns)):
            table[columns[e]].append(instance[e])
    
    df = pd.DataFrame(table)
    
    data_exporting(df)

    return 0

if __name__ == "__main__":
    main()
