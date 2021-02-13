import requests
import csv
import os


def collecting_New_data():

    r = requests.get('http://api.worldweatheronline.com/premium/v1/weather.ashx?key=74a87fc92c714e70aa1112002210101&q=Rawalpindi&format=json&num_of_days=2&fx24=3').json()
    os.chdir(r"NewFile")
    c = csv.writer(open("NewWeather.csv", "w"), lineterminator='\n')
    header = ["time", "winddirDegree", "WindGustKmph", "HeatIndexC", "WindChillC", "visibility", "humidity"]
    c.writerow(header)
    for items in r['data']['weather']:
        for new_items in items['hourly']:
            c.writerow([new_items['time'], new_items['winddirDegree'], new_items['WindGustKmph'], new_items['HeatIndexC'], new_items['WindChillC'], new_items['visibility'], new_items['humidity']])

collecting_New_data()