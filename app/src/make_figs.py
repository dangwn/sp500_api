'''
Author: Dan Gawne
Date: 2021-02-09
'''

import matplotlib.pyplot as plt
import mpld3
import datetime as dt

def create_day_range(
    start : dt.datetime,
    end : dt.datetime
) -> list:
    dates = []
    d = start
    excluded = (6,7)

    while d.date() <= end.date():
        if d.isoweekday() not in excluded:
            dates.append(d)
        d += dt.timedelta(days=1)
    return dates

def plot_to_html(fig):
    return mpld3.fig_to_html(fig)

# TODO:
#  Add dates to plot - having 3/4 dates on the bottom at regular intervals
def create_raw_plot(
    data,
    ticker = None, currency = None,
    start = None, end = None,
):
    fig, ax = plt.subplots(figsize=(12,6))
    
    ax.plot(data, color='green', linewidth='1.5')
    ax.set_ylabel('Adjusted Close Price')
    ax.grid()

    title = (f'{ticker.upper()} ' if ticker is not None else '') + (f'({currency})' if currency is not None else '')
    ax.set_title(title)
    
    return fig
