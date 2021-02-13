import pandas as pd
import numpy as np
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from joblib import dump, load
import joblib
def Wind_Pred():
    dataset = pd.read_csv(r"Rawalpindi.csv",index_col='date_time',parse_dates=True)
    X = dataset[['WindGustKmph', 'winddirDegree']].values
    Y = dataset['windspeedKmph'].values
    X_train, X_test, Y_train, _ = train_test_split(X, Y, test_size=0.20, random_state=42)
    regressor = RandomForestRegressor(n_estimators=500, random_state=0)
    regressor.fit(X_train,Y_train)
    _ = regressor.predict(X_test)
    # print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, predictData))
    # print('Mean Squared Error:', metrics.mean_squared_error(Y_test, predictData))
    # print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, predictData)))
    dump(regressor, 'RFRegWIND.joblib')
Wind_Pred()