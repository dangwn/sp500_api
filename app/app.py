'''
Author: Dan Gawne
Date: 2021-02-09
'''

from flask import Flask, request, url_for
import waitress
import json
import requests

from src import make_figs
from src.request_yahoo import request_yahoo

#--------------------------------------------------------------------------------------------------
# Error Message
#--------------------------------------------------------------------------------------------------
def error_msg(msg : str):
    return json.dumps({'error' : msg})

#--------------------------------------------------------------------------------------------------
# App
#--------------------------------------------------------------------------------------------------
app = Flask(__name__)

@app.route('/')
def index():
    return "It's up and running"

@app.route('/sp-data', methods=['POST'])
def get_sp_data():
    try:
        data = json.loads(request.data)
        if data is None:
            return error_msg('Problem with loading request...')

        return request_yahoo(data)
    except:
        return error_msg('Something went wrong...')

@app.route('/sp-graph', methods=['POST'])
def get_sp_graph():
    try:
        data = json.loads(request.data)
        if data is None:
            return error_msg('Problem with loading request...')

        response_data = json.loads(request_yahoo(data))

        fig = make_figs.create_raw_plot(
            data = response_data.get('adjclose', None),
            ticker = data.get('ticker', None),
            currency = response_data.get('currency', None)
            # Add start and end points
        )

        return json.dumps({'plot_html' : make_figs.plot_to_html(fig), 'error' : None})


    except:
        return error_msg('Something went wrong...')
    
if __name__ == '__main__':
    waitress.serve(app, host='0.0.0.0', port=444)