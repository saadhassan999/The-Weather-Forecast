from joblib import dump, load
import numpy as np
import pandas as pd


def Final_Temp_Pred():
    model = load(r"RFRegTemp.joblib") 
    new_dataset = pd.read_csv(r"~/theweatherforecast/NewFile/NewWeather.csv")
    X_New = new_dataset[['WindChillC', 'HeatIndexC']].values
    Final_Temp_Pred.forecast = model.predict(X_New)
Final_Temp_Pred()
def showTempForecast():
    return Final_Temp_Pred.forecast.astype(int)
print(showTempForecast())
