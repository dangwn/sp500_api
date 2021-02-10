'''
Author: Dan Gawne
Date: 2021-02-09
'''

from flask import Flask, request
import waitress
import json

from src import get_data

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
        if data == None:
            return error_msg('Problem with loading data...')
        
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

    except:
        return error_msg('Something went wrong...')

@app.route('/sp-graph', methods=['POST'])
def get_sp_graph():


    return
    
if __name__ == '__main__':
    waitress.serve(app, host='0.0.0.0', port=444)