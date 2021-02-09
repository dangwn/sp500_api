from app.src import make_figs
import datetime as dt

def test_date_range():
    start = dt.datetime(2019,1,21)
    end = dt.datetime(2019,1,30)

    assert len(make_figs.create_day_range(start, end)) == 8
    
