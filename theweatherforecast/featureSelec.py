# import pandas as pd
# import numpy as np
# import datetime as dt
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestRegressor

# dataset = pd.read_csv(r"C:\Users\saadh\Desktop\theweatherforecast\theweatherforecast\theweatherforecast\Rawalpindi.csv",index_col='date_time',parse_dates=True)
# X = dataset.drop(['moonrise', 'moonset', 'sunrise', 'sunset','location','precipMM'], axis=1)
# Y = dataset['precipMM'].values
# regressor = RandomForestRegressor(n_estimators=500, random_state=0)
# regressor.fit(X,Y)
# feat_importances = pd.Series(regressor.feature_importances_, index=X.columns)
# feat_importances.nlargest(20).plot(kind='barh')
