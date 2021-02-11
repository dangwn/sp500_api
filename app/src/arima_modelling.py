'''
Author: Dan Gawne
Date: 2021-02-11
'''

from statsmodels.tsa.arima_model import ARIMA
import numpy as np

# TODO: Auto find p,d and q for arima model
def arima_predictions(
    data,
    num_future_days = 7
):

    # Adjust for volitility
    log_price = np.log(data)
    model = ARIMA(log_price,order=(3,1,0)).fit(disp = 0)

    y_hat = model.predict(
        len(data)+1, len(data) + num_future_days, typ='levels'
    )

    # Undo log
    return np.exp(y_hat)
