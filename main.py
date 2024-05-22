import pandas as pd

# Wczytanie danych
url = "https://gist.githubusercontent.com/Wiktor0000/73a321d9dacfa3f67e05cef585001532/raw/5213dbcca77a21e8d00a8e0201ca488eea9b4f23/gistfile1.txt"
data_frame = pd.read_csv(url, sep=';')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(data_frame)
