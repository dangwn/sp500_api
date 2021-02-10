'''
Author: Dan Gawne
Date: 2021-02-10
'''

from . import get_data

def error_msg(msg : str):
    return json.dumps({'error' : msg})

def request_yahoo(data : str) -> str:  
    ticker = data.get('ticker', None)
    if ticker is None:
        return error_msg('Problem with loading ticker...')

    start      = data.get('start', None)
    end        = data.get('end', None)
    proxy      = data.get('proxy', None)
    return_all = data.get('return_all', False)

    return get_data.get_json(
        ticker = ticker,
        start = start,
        end = end,
        proxy = proxy,
        return_all = return_all
    )

