import pandas as pd
from random import randint
import generators as gen 
# import matplotlib.pyplot as plt
# import math



def main():
    count = randint(70_000, 140_000)

    columns = ['First Name', 'Middle Name', 'Last Name', 'Date', "Session's time", "Day time",
                # "Day of the week", 'Weekend', 
                "Film", "Genre", 'Hall', "Row", "Seat", "Ticket's Price"]
    table = {}
    for i in columns:
        table[f'{i}'] = []
    
    for i in range(count):
        instance = [
            gen.clients_fname(), gen.c_mname(), gen.c_lname(), 
            gen.random_date(), gen.sessions_time(), gen.day_time(), 
            #gen.day_of_the_week(),
            # gen.doff_or_weekd(), 
            gen.film(), gen.genre(),
            gen.hall_num(), gen.row(), gen.seat(), gen.pricing()
        ]

        for e in range(len(columns)):
            table[columns[e]].append(instance[e])
    
    df = pd.DataFrame(table)

    df.to_excel('./table.xlsx')
    # df.to_sql('./table.sql') 
    
    return 0

if __name__ == "__main__":
    main()
