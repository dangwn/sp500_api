'''
Author: Dan Gawne
Date: 2021-02-11
'''

from statsmodels.tsa.arima_model import ARIMA


import pandas as pd
import numpy as np

def static_arima_predictions(
    data,
    lags = 1, trend = 'c',
    num_future_days = 7
):

    log_price = np.log(data)
    model = ARIMA(log_price,order=(0,1,0)).fit(disp = 0)

    y_hat = model.predict(
        len(data), len(data) + num_future_days, typ='levels'
    )

    return np.exp(y_hat)

if __name__ == '__main__':
    data = [(i + (np.random.uniform() - 0.5)) for i in range(1,100)]
    y_hat = auto_reg_predictions(data)

    print('\n\n')
    print(data)
    print(y_hat)

