'''
Author: Dan Gawne
Date: 2021-02-09
'''

import matplotlib.pyplot as plt
import mpld3
import datetime as dt

from . import arima_modelling

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

def create_raw_plot(
    data,
    ticker = None, currency = None,
    start = None, end = None,
):
    fig, ax = plt.subplots(figsize=(12,6))
    
    xticks = range(len(data))
    # I have 1000000% cheated with this bit, but thug life baby 
    if start is not None and end is not None and len(data) < (366*5):
        start_dt = dt.datetime.fromtimestamp(start)
        end_dt   = dt.datetime.fromtimestamp(end)

        raw_date_range = create_day_range(start_dt,end_dt)
        mod_date_range = raw_date_range[(len(raw_date_range) - len(data)):]

        if len(mod_date_range) == len(data):
            xticks = (mod_date_range) 

    ax.plot(xticks, data, color='green', linewidth='1.5')
    ax.set_ylabel('Adjusted Close Price')
    ax.grid()

    title = (f'{ticker.upper()} ' if ticker is not None else '') + (f'({currency})' if currency is not None else '')
    ax.set_title(title)

    return fig, ax


def create_arima_plot(
    data,
    ticker = None, currency = None,
    start = None, end = None,
    num_future_days = 14
):
    fig, ax = create_raw_plot(data[-30:], ticker, currency, start, end)

    preds = arima_modelling.arima_predictions(data, num_future_days=7)
    
    end_dt = dt.datetime.fromtimestamp(end)
    new_dates = [end_dt]
    while (len(new_dates) < len(preds)):
        end_dt += dt.timedelta(days = 1)
        new_dates.append(end_dt)


    ax.plot(new_dates, preds, color = 'red', linewidth='3')

    

    return fig, ax

