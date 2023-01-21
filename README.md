# ads-rework
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
filename = "world_bank_data.csv"
df = pd.read_csv(filename)
country_codes = ['BRA', 'JPN', 'USA', 'IND', 'CHN'] 
years = ["2005", "2008", "2010", "2012", "2015", "2018"]
# list of indicators for the country
indicator_names = [
    "Population growth (annual %)",
    "Nitrous oxide emissions (% change from 1990)",
    "Methane emissions (kt of CO2 equivalent)",
    "Forest area (sq. km)",
    "Agricultural land (sq. km)",
    "CO2 emissions (kg per PPP $ of GDP)",
]
