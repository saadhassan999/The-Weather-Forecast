from joblib import dump, load
import numpy as np
import pandas as pd

def Final_Prec_Pred():
    model = load(r"RFRegPrecp.joblib") 
    new_dataset = pd.read_csv(r"~/theweatherforecast/NewFile/NewWeather.csv")
    X_New = new_dataset[['visibility', 'humidity', 'WindGustKmph']].values
    Final_Prec_Pred.forecast = model.predict(X_New)
Final_Prec_Pred()
def showPrecpForecast():
    return Final_Prec_Pred.forecast.astype(int)
print(showPrecpForecast())