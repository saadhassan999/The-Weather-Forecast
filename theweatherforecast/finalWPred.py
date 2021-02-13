from joblib import dump, load
import numpy as np
import pandas as pd

def Final_Wind_Pred():
    model = load(r"RFRegWIND.joblib") 
    new_dataset = pd.read_csv(r"~/theweatherforecast/NewFile/NewWeather.csv")
    X_New = new_dataset[['WindGustKmph', 'winddirDegree']].values
    Final_Wind_Pred.forecast = model.predict(X_New)
Final_Wind_Pred()
def showWindForecast():
    return Final_Wind_Pred.forecast.astype(int)
print(showWindForecast())