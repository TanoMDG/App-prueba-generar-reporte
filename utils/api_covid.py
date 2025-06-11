import requests
import pandas as pd

URL = "https://pomber.github.io/covid19/timeseries.json"

def get_data_country(country):
    all_data = requests.get(URL).json()
    df = pd.DataFrame(all_data.get(country, []))
    df['date'] = pd.to_datetime(df['date'])
    return df
