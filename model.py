import pickle
import catboost
import pandas as pd

MODEL_PATH = 'models/cat_model.pkl'
SCALER_PATH = 'models/scaler.pkl'

columns = ['Площадь о', 'Этаж 1',  
            'Район_Ленинский',
           'Район_Ленинский (Левый берег)', 'Район_Орджоникидзевский',
           'Район_Орджоникидзевский (левый берег)', 'Район_Правобережный'
            ]


def load_model():
    return  pickle.load(open(MODEL_PATH, 'rb'))

def load_scaler():    
    return  pickle.load(open(SCALER_PATH, 'rb'))

def get_prediction(square, n_floor, district_len, district_len_left, district_ordg, district_ordg_left, district_right):
    cat = load_model()
    scaler = load_scaler()
    
    data = [square, n_floor, district_len, district_len_left, district_ordg, district_ordg_left, district_right]
    df = pd.DataFrame(scaler.transform([data]))
    df = df.astype(float)
    df.columns = columns
    result = cat.predict(df)
    prediction = pd.DataFrame(data=result, columns=['Price'])
    
    return prediction.reset_index(drop=True)