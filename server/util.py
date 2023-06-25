import json
import pickle
import pandas as pd
import numpy as np

def get_data_columns():
    global data_cols
    with open("../artifacts/columns.json",'r') as f:
        data_cols = json.load(f)['data_columns']
    return data_cols

def get_locations():
    return data_cols[4:]

def get_model():
    global model
    with open("../artifacts/home_prices_model.pickle",'rb') as f:
        model = pickle.load(f)

def predict_price(location,sqft,bath,bedrooms,balcony):
    try: #list can through error if location is not found
        loc_index = data_cols.index(location) 
    except:
        loc_index = -1
    x = np.zeros(len(data_cols))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bedrooms
    if loc_index >= 0:
        x[loc_index] = 1
    df = pd.DataFrame([x], columns = data_cols)
    
    return round(model.predict(df)[0],2)

if __name__ == "__main__":
    get_data_columns()
    get_model()
    # print(get_locations())
    # print(predict_price('1st Phase JP Nagar',1000, 3, 3, 1))