import pickle
import numpy as np


def percent(hour):
    filename = '/Users/mac/Desktop/GRIP/task1/firstTask/regression_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    own_pred = loaded_model.predict(np.array([hour]).reshape(-1, 1))
    res = float("{:.2f}".format(own_pred[0]))
    if res >= 100.00:
        return 100.00
    else:
        return res



