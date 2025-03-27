import json
import pickle
import numpy as np
__locations=None
__datacolumns=None
__model=None


def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __datacolumns.index(location.lower())
    except:
        loc_index=-1

    x = np.zeros(len(__datacolumns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return  __locations


def get_location_artifacts():
    print("Loading artifacts...start")
    global __datacolumns
    global __locations
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __datacolumns = json.load(f)['data_columns']
        __locations = __datacolumns[3:]

    with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print("Loading Saved artifacts...done")


import json

with open('./artifacts/columns.json', 'r') as f:
    data = json.load(f)
    print(data.keys())  # Should print 'data_columns'

if __name__ == '__main__':
    get_location_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st phase jp naga',1000,3,2))



