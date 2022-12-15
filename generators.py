from random import randint
from datetime import date
import random_names



HALL = [
            [400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 400, 400, 400, 400, 400],
            [400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 400, 400, 400, 400, 400],
            [400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 400, 400, 400, 400, 400],
            [600, 600, 600, 600, 600, 1000, 1000, 1000, 1000, 1000, 600, 600, 600, 600, 600],
            [800, 800, 800, 800, 800, 2000, 2000, 2000, 2000, 2000, 800, 800, 800, 800, 800],
            [800, 800, 800, 800, 800, 2000, 2000, 2000, 2000, 2000, 800, 800, 800, 800, 800],
            [600, 600, 600, 600, 600, 1000, 1000, 1000, 1000, 1000, 600, 600, 600, 600, 600],
            [400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 400, 400, 400, 400, 400],
            [400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 400, 400, 400, 400, 400],
            [400, 400, 400, 400, 400, 800, 800, 800, 800, 800, 400, 400, 400, 400, 400]
        ]
    
FILMS = ["Брат", "Брат 2", "Груз-200", "Курьер", "Терминал",
            "Однажды в Голливуде", "Бесславные Ублюдки",
            "Все ненавидят Йохана", "Сделано в Америе", "Золото",
            "Трамбо", "Оно", "Оно 2", "Малыш на драйве", "Драйв",
            "Стрелок", "Кингсман. Секретная миссия", "Телефонная будка",
            "Шоу Трумана", "Лицо со шрамом", "Волк с Уолл-Стрит",
            "Операция Колибри", "Паразиты"]

GENRES = ["Боевик", "Боевик", "Триллер", "Триллер",
            "Драма", "Вестерн", "Боевик", "Трагикомедия",
            "Боевик", "Боевик", "Приключения", "Ужас", "Ужас",
            "Триллер", "Боевик", "Боевик", "Боевик", "Трагедия",
            "Драма", "Боевик", "Комедия", "Детектив", "Трагедия"]

def clients_fname():
    return random_names.First()

def c_mname():
    return random_names.Middle()

def c_lname():
    return random_names.Last()

def random_date():
    global year, month, day
    year = 2022
    month = randint(6, 12)
    if month in [6, 9, 11]:
        day = randint(1, 30)
    else:
        day = randint(1, 31)
    
    return '{}:{}:{}'.format(day, month, year)

def sessions_time():
    global hour
    hour = randint(0, 23)
    minutes = randint(0, 1)
    if minutes:
        minutes = 30
        return f"{hour}:{minutes}"
    else:
        minutes = "00"
        return f"{hour}:{minutes}"

def day_time():
    if hour > 20 and hour < 5:
        return 'night'
    return 'day'

# def doff_or_weekd():
#     global dotw
#     dotw = date.weekday(year, month, day)
#     if dotw > 4:
#         return 0
#     return 1

# def day_of_the_week():
#     days = ['Monday', 'Tuesday', 'Wednsday', 'Thirsday', 'Friday', 'Saturday', 'Sunday']
#     i = dotw
#     return days[i]


def film():
    global cinema_id
    cinema_id = randint(0, 22)

    return FILMS[cinema_id]

def genre():
    return GENRES[cinema_id]

def hall_num():
    return f"{randint(1, 25)}"


def row():
    global rw
    rw = randint(0, 9)
    return rw + 1

def seat():
    global st
    st = randint(0, 14)
    return st + 1

def pricing():
    return HALL[rw][st]

def main():
    return 0

if __name__ == '__main__':
    main()
