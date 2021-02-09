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


