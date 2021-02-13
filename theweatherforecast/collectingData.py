from wwo_hist import retrieve_hist_data
import os
import urllib.request
from datetime import datetime, timedelta, date


def collecting_data():
    today_date = date.today()
    yesterday_date = today_date - timedelta(1)
    os.chdir(r"theweatherforecast")
    frequency=3
    start_date = '2015-01-01'
    end_date = yesterday_date.strftime('%Y-%B-%d')
    api_key = '74a87fc92c714e70aa1112002210101'
    location_list = ['Rawalpindi']
    _ = retrieve_hist_data(api_key,
                                    location_list,
                                    start_date,
                                    end_date,
                                    frequency,
                                    location_label = False,
                                    export_csv = True,
                                    store_df = True)
collecting_data()