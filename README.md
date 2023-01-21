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
def read_wb_data(filename):
    """
        Input:
            filename: the name of the .csv file
        Output: 
            df_years: a dataframe with the years from 1960 to 2021
            df_countries: a dataframe with the countries 
    """
    df = pd.read_csv(filename, index_col = 0)
    df_years = df.drop(['Country Code','Indicator Name','Indicator Code'], axis=1)
    df_countries = df.drop(['Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'], axis=1).transpose()
    return (df_years, df_countries)
