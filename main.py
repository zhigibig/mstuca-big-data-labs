import pandas as pd
from random import randint



def date_type(day, month, year):
    return f"{day}:{month}:{year}"

def times_of_day_type():
    arr = ["day", "night"]
    return arr[randint(0, 1)]

def day_of_the_week_type():
    days = ["week day", "day off"]
    return days[randint(0, 1)]

def time_type():
    hour = randint(1, 23)
    minutes = randint(0, 1)
    if minutes:
        minutes = 30
        return f"{hour}:{minutes}"
    else:
        minutes = "00"
        return f"{hour}:{minutes}"

def film_type():
    films = ["Брат", "Брат 2", "Груз-200", "Курьер", "Терминал",
             "Одныжды в Голливуде", "Бесславные Ублюдки",
             "Все ненавидят Йохана", "Сделано в Америе", "Золото",
             "Трамбо", "Оно", "Оно 2", "Малыш на драйве", "Драйв",
             "Стрелок", "Кингсман. Секретная миссия", "Телефонная будка",
             "Шоу Трумана", "Лицо со шрамом", "Волк с Уолл-Стрит",
             "Операция Колибри", "Паразиты"]
    return films[randint(0, len(films) - 1)]

def genre_type():
    genres = ["Боевик", "Боевик", "Триллер", "Триллер",
              "Драма", "Вестерн", "Боевик", "Трагикомедия",
              "Боевик", "Боевик", "Приключения", "Ужас", "Ужас",
              "Триллер", "Боевик", "Боевик", "Боевик", "Трагедия",
              "Драма", "Боевик", "Комедия", "Детектив", "Трагедия"]
    return genres[randint(0, len(genres) - 1)]

def cinema_hall_type():
    return f"{randint(0, 25)}"

def row_type():
    return randint(0, 10)

def seat_type():
    return randint(0, 15)

def price_type():
    arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000]
    return arr[randint(0, len(arr) - 1)]

def main():
    count = 5000
    df = pd.DataFrame({
        "Film": [film_type() for i in range(count)],
        "Genre": [genre_type() for i in range(count)],
        "Date": [date_type(randint(1, 30), randint(1, 12), 2021) for i in range(count)],
        "Day of the Week": [day_of_the_week_type() for i in range(count)],
        "Time of the day": [times_of_day_type() for i in range(count)],
        "Hall": [cinema_hall_type() for i in range(count)],
        "Row": [row_type() for i in range(count)],
        "Seat": [seat_type() for i in range(count)],
        "Session time": [time_type() for i in range(count)],
        "Price of ticket": [price_type() for i in range(count)],
    })

    df.to_excel('./table.xlsx')
    # df.to_sql('./') 
    
    return 0

if __name__ == "__main__":
    main()
