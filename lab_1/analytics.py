import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
import os
from addresses_of_files import excel_table_adress
from data_generators import FILMS, HALL



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

    global ROWS, SEATS
    ROWS = df_list['Row']
    SEATS = df_list['Seat']

    return 0

def show_table():
    
    os.system('open {excel_table_adress}')

    return 0

plt.show()

def seats_prices():
    
    row = [f'row {i + 1}' for i in range(10)]
    seat = [f'seat {i + 1}' for i in range(15)]

    fig, ax = plt.subplots()

    h = np.array(HALL)

    im = ax.imshow(HALL)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(seat)), labels=seat)
    ax.set_yticks(np.arange(len(row)), labels=row)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(row)):
        for j in range(len(seat)):
            text = ax.text(j, i, h[i, j],
                        ha="center", va="center", color="w")

    ax.set_title("Price")
    fig.tight_layout()

    plt.show()

    return 0

def seats_popularity():

    tickets_per_place = [[0 for i in range(15)] for i in range(10)]

    for i in range(len(ROWS)):
        y = ROWS[i] - 1
        x = SEATS[i] - 1
        tickets_per_place[y][x] += 1

    row = [f'row {i + 1}' for i in range(10)]
    seat = [f'seat {i + 1}' for i in range(15)]

    h = np.array(tickets_per_place)
    
    def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
        """
        Create a heatmap from a numpy array and two lists of labels.

        Parameters
        ----------
        data
            A 2D numpy array of shape (M, N).
        row_labels
            A list or array of length M with the labels for the rows.
        col_labels
            A list or array of length N with the labels for the columns.
        ax
            A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
            not provided, use current axes or create a new one.  Optional.
        cbar_kw
            A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
        cbarlabel
            The label for the colorbar.  Optional.
        **kwargs
            All other arguments are forwarded to `imshow`.
        """

        if ax is None:
            ax = plt.gca()

        if cbar_kw is None:
            cbar_kw = {}

        # Plot the heatmap
        im = ax.imshow(data, **kwargs)

        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        # Show all ticks and label them with the respective list entries.
        ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
        ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

        # Let the horizontal axes labeling appear on top.
        ax.tick_params(top=True, bottom=False,
                    labeltop=True, labelbottom=False)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
                rotation_mode="anchor")

        # Turn spines off and create white grid.
        ax.spines[:].set_visible(False)

        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
        ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False)

        return im, cbar


    def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
        """
        A function to annotate a heatmap.

        Parameters
        ----------
        im
            The AxesImage to be labeled.
        data
            Data used to annotate.  If None, the image's data is used.  Optional.
        valfmt
            The format of the annotations inside the heatmap.  This should either
            use the string format method, e.g. "$ {x:.2f}", or be a
            `matplotlib.ticker.Formatter`.  Optional.
        textcolors
            A pair of colors.  The first is used for values below a threshold,
            the second for those above.  Optional.
        threshold
            Value in data units according to which the colors from textcolors are
            applied.  If None (the default) uses the middle of the colormap as
            separation.  Optional.
        **kwargs
            All other arguments are forwarded to each call to `text` used to create
            the text labels.
        """

        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()

        # Normalize the threshold to the images color range.
        if threshold is not None:
            threshold = im.norm(threshold)
        else:
            threshold = im.norm(data.max())/2.

        # Set default alignment to center, but allow it to be
        # overwritten by textkw.
        kw = dict(horizontalalignment="center",
                verticalalignment="center")
        kw.update(textkw)

        # Get the formatter in case a string is supplied
        if isinstance(valfmt, str):
            valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

        # Loop over the data and create a `Text` for each "pixel".
        # Change the text's color depending on the data.
        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
                texts.append(text)

        return texts

    fig, ax = plt.subplots()

    im, cbar = heatmap(h, row, seat, ax=ax,
                    cmap="YlGn", cbarlabel="number of tickets (in thousands)")
    texts = annotate_heatmap(im, valfmt="{x}")

    fig.tight_layout()
    plt.show()

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

    plt.plot([i for i in range(1, len(calendar) + 1)], values)

    plt.ylabel('Number of visitor per a day')
    
    plt.xlabel('Dates (first day - 1/06/2022, last day - 31/12/2022)')

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

    show_table()

    number_of_visitors()

    time_of_day_popularity()

    genres_popularity()

    fimls_popularity()

    seats_prices()

    seats_popularity()

    return 0

if __name__ == '__main__':
    main()
