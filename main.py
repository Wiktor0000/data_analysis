import pandas as pd

# Wczytanie danych
url = "https://gist.githubusercontent.com/Wiktor0000/6860ca399b57170d2d2c423d442e5037/raw/b7b571f2fc52d3ab6a9e6de2b58d99186a92fbad/data_project.csv"
data_frame = pd.read_csv(url, sep=';')

data_frame.columns = data_frame.columns.str.replace(' _', '_')
data_frame["zanieczyszczenie_powietrza"] = data_frame["zanieczyszczenie_powietrza"].str.replace(',', '.').astype(float)
data_frame["liczba_osob_z_wyksztalceniem_wyzszym_(%)"] = data_frame["liczba_osob_z_wyksztalceniem_wyzszym_(%)"].str.replace(',', '.').astype(float)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(data_frame)

average_pollution = data_frame["zanieczyszczenie_powietrza"].mean()
print(f"Average pollution: {average_pollution:.2f}")
