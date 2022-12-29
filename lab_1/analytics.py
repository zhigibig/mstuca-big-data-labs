import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from addresses_of_files import excel_table_adress
from data_generators import FILMS



GENRES = [
            "Боевик", "Триллер", "Драма", "Вестерн", 
            "Трагикомедия", "Приключения", "Ужас",
            "Трагедия", "Комедия", "Детектив",
        ]



def parsing_excel_table():
    file = excel_table_adress
    xl = pd.ExcelFile(file)

    global df
    df = xl.parse('Sheet1')

    return 0

def data_defragmentation():
    global df_list 
    df_list = df.to_dict('list')

    global DATES
    DATES = df_list['Date']

    return 0

def seats_popularity():

    

    return 0

def genres_popularity():
    fig, ax = plt.subplots()

    values = [df_list['Genre'].count(i) for i in GENRES]

    bar_labels = GENRES
    bar_colors = [
        'red', 'tab:orange', 'tab:blue',
        'tab:purple', 'tab:grey', 'tab:brown',
        'tab:green', 'tab:cyan', '#444b52', 
        '#fcd544'
        ]

    ax.bar([i for i in range(1, 11)], values, label = bar_labels, color = bar_colors)

    ax.set_ylabel('Number of tickets')
    ax.set_title('Popularity of different genres')
    ax.legend(title='Genres colors')

    plt.show()

    return 0

def fimls_popularity():
    fig, ax = plt.subplots()

    values = [df_list['Film'].count(i) for i in FILMS]

    bar_labels = FILMS
    bar_colors = [
        'red', 'tab:orange', 'tab:blue',
        'tab:purple', 'tab:grey', 'tab:brown',
        'tab:green', 'tab:cyan', '#444b52', 
        '#fcd544'
        ]

    ax.bar([i for i in range(1, 24)], values, label = bar_labels, color = bar_colors)

    ax.set_ylabel('Number of tickets')
    ax.set_title('Popularity of different films')
    ax.legend(title='Colors of films')

    plt.show()

    return 0

def sessions_popularity():



    return 0

def number_of_visitors():

    calendar = []

    for month in range(6, 10):
        if month in [6, 9, 11]:
            for day in range(1, 30 + 1):
                date = f'{day}/{month}/2022'
                if date in DATES:
                    calendar.append(date)
        else:
            for day in range(1, 31 + 1):
                date = f'{day}/{month}/2022'
                if date in DATES:
                    calendar.append(date)

    values = []

    for i in calendar:
        values.append(DATES.count(i))



    plt.plot(calendar, values)

    plt.ylabel('Number of visitor per a day')
    
    plt.xlabel('Dates')

    plt.title('Visitor growth chart')

    plt.show()

    return 0

def time_of_day_popularity():
    fig, ax = plt.subplots()

    day_times = ['day', 'night']

    number_of_daily_sessions = df_list['Day time'].count('day')
    number_of_night_sessions = len(df_list['Day time']) - number_of_daily_sessions
    values = [number_of_daily_sessions, number_of_night_sessions]

    bar_labels = ['Day', 'Night']
    bar_colors = ['#fcd544', '#444b52']

    ax.bar(day_times, values, label = bar_labels, color = bar_colors)

    ax.set_ylabel('number of sessions')
    ax.set_title('Popularity of daily and night sessions')
    ax.legend(title='Time of the day color')

    plt.show()
    
    return 0

def main():
    parsing_excel_table()

    data_defragmentation()

    time_of_day_popularity()

    genres_popularity()

    fimls_popularity()

    # seats_popularity()
    
    # sessions_popularity()

    number_of_visitors()

    return 0

if __name__ == '__main__':
    main()
