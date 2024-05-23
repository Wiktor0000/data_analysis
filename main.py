import pandas as pd

# Wczytanie danych
url = "https://gist.githubusercontent.com/Wiktor0000/6860ca399b57170d2d2c423d442e5037/raw/b7b571f2fc52d3ab6a9e6de2b58d99186a92fbad/data_project.csv"
data_frame = pd.read_csv(url, sep=';')

data_frame.columns = data_frame.columns.str.replace(' _', '_')
data_frame["zanieczyszczenie_powietrza"] = data_frame["zanieczyszczenie_powietrza"].str.replace(',', '.').astype(float)
data_frame["liczba_osob_z_wyksztalceniem_wyzszym_(%)"] = data_frame["liczba_osob_z_wyksztalceniem_wyzszym_(%)"].str.replace(',', '.').astype(float)
data_frame["gdp_per_capita"] = data_frame["gdp_per_capita"].str.replace(',', '.').astype(float)
data_frame["stopa_bezrobocia"] = data_frame["stopa_bezrobocia"].str.replace(',', '.').astype(float)
data_frame["liczba_lekarzy_na_1000_osob"] = data_frame["liczba_lekarzy_na_1000_osob"].str.replace(',', '.').astype(float)
data_frame["stopa_stabilnosci_politycznej"] = data_frame["stopa_stabilnosci_politycznej"].str.replace(',', '.').astype(float)
pd.options.display.float_format = "{:.2f}".format

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(data_frame)
print()

# średnia_zanieczyszczenie powietrza
avg_pollution = data_frame["zanieczyszczenie_powietrza"].mean()
std_pollution = data_frame["zanieczyszczenie_powietrza"].std()
vk_pollution = std_pollution / avg_pollution
print(f"Average - pollution: {avg_pollution:.2f}")
print(f"Deviation - pollution: {std_pollution:.2f}")
print(f"Variation coefficient - pollution: {vk_pollution:.2f}")
print()

#średnia_liczba osób z wykształceniem wyższym (%)
avg_higher_education = data_frame["liczba_osob_z_wyksztalceniem_wyzszym_(%)"].mean()
std_higher_education = data_frame["liczba_osob_z_wyksztalceniem_wyzszym_(%)"].std()
vk_higher_education = std_higher_education / avg_higher_education
print(f"Average - higher education: {avg_higher_education:.2f}")
print(f"Deviation - higher education: {std_higher_education:.2f}")
print(f"Variation coefficient - higher education: {vk_higher_education:.2f}")
print()

#średnia_gdp per capita
avg_gdp = data_frame["gdp_per_capita"].mean()
std_gdp = data_frame["gdp_per_capita"].std()
vk_gdp = std_gdp / avg_gdp
print(f"Average - GDP per capita: {avg_gdp:.2f}")
print(f"Deviation - GDP per capita: {std_gdp:.2f}")
print(f"Variation coefficient - gdp: {vk_gdp:.2f}")
print()

#średnia_stopa bezrobocia
avg_unemployment_rate = data_frame["stopa_bezrobocia"].mean()
std_unemployment_rate = data_frame["stopa_bezrobocia"].std()
vk_unemployment_rate = std_unemployment_rate / avg_unemployment_rate
print(f"Average - unemployment rate: {avg_unemployment_rate:.2f}")
print(f"Deviation - unemployment rate: {std_unemployment_rate:.2f}")
print(f"Variation coefficient - unemployment rate: {vk_unemployment_rate:.2f}")
print()

#średnia_liczba lekarzy na 1000 osób
avg_amount_of_doctor = data_frame["liczba_lekarzy_na_1000_osob"].mean()
std_amount_of_doctor = data_frame["liczba_lekarzy_na_1000_osob"].std()
vk_amount_of_doctor = std_amount_of_doctor / avg_amount_of_doctor
print(f"Average - amount of doctors per 1000 people: {avg_amount_of_doctor:.2f}")
print(f"Deviation - amount of doctors per 1000 people: {std_amount_of_doctor:.2f}")
print(f"Variation coefficient - amount of doctors per 1000 people: {vk_amount_of_doctor:.2f}")
print()

#średnia_stopa stabilnośc politycznej
avg_political_stability_rate = data_frame["stopa_stabilnosci_politycznej"].mean()
std_political_stability_rate = data_frame["stopa_stabilnosci_politycznej"].std()
vk_political_stability_rate = std_political_stability_rate / avg_political_stability_rate
print(f"Average - political stability rate: {avg_political_stability_rate:.2f}")
print(f"Deviation - political stability rate: {std_political_stability_rate:.2f}")
print(f"Variation coefficient - politicial stability rate: {vk_political_stability_rate:.2f}")
print()