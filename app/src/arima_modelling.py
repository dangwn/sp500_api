'''
Author: Dan Gawne
Date: 2021-02-11
'''

from statsmodels.tsa.arima_model import ARIMA
import numpy as np

# TODO: Auto find p,d and q for arima model
def static_arima_predictions(
    data,
    lags = 1, trend = 'c',
    num_future_days = 7
):

    # Adjust for volitility
    log_price = np.log(data)
    model = ARIMA(log_price,order=(0,1,0)).fit(disp = 0)

    y_hat = model.predict(
        len(data), len(data) + num_future_days, typ='levels'
    )

    # Undo log
    return np.exp(y_hat)

