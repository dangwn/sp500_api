'''
Author: Dan Gawne
Date: 2021-02-09
'''

import requests
import pandas as pd
import json
import time
import datetime

def get_json(
    ticker : str,
    start = None, end = None,
    proxy = None,
    return_all = False
) -> str:
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker.upper()}'

    params = {}
    
    # Start Point
    if start is None:
        start = -2208988800
    elif isinstance(start, datetime.datetime):
        start = int(time.mktime(start.timetuple()))
    else:
        start = int(time.mktime(
            time.strptime(str(start), '%Y-%m-%d')))

    # End Point
    if end is None:
        end = int(time.time())
    elif isinstance(end, datetime.datetime):
        end = int(time.mktime(end.timetuple()))
    else:
        end = int(time.mktime(time.strptime(str(end), '%Y-%m-%d')))


    params['period1'] = start
    params['period2'] = end
    params['interval'] = '1d'.lower()
    params['includePrePost'] = False
    params['events'] = 'div,splits'

    data = requests.get(url=url, params=params, proxies=proxy)
    if 'Will be right back' in data.text:
        raise RuntimeError('*** YAHOO! FINANCE IS CURRENTLY DOWN! ***\n'
                            'Our engineers are working quickly to resolve '
                            'the issue. Thank you for your patience.')
    data = data.json()

    if return_all:
        return data

    return json.dumps({
        'adjclose' : data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose'],
        'currency' : data['chart']['result'][0]['meta']['currency'],
        'error'    : data['chart']['error']
    })
    
    



if __name__ == '__main__':
    data = json.loads(get_json(
        'MSFT',
        start = datetime.datetime(2021,1,1), end = datetime.datetime(2021,2,1)
    ))
    print(len(data['adjclose']))
    