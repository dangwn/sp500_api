from app.src import get_data
import datetime
import json

def test_get_json_response():
    data = json.loads(get_data.get_json(
        'MSFT',
        start = datetime.datetime(2021,1,1), end = datetime.datetime(2021,2,1)
    ))

    assert data['error'] == None

def test_get_json_data():
    data = json.loads(get_data.get_json(
        'AAPL',
        start = datetime.datetime(2021,1,1), end = datetime.datetime(2021,2,1)
    ))

    assert type(data['adjclose']) == list
    assert len(data['adjclose']) == 19


    