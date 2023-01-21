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
# years,countries = read_wb_data(filename)


def data_plots(indicator_name):
    """This function takes indicator name as argument, It plots the line plot for the dataframe and
    returns the filtered dataframe for the indicator with given countries and years"""

#     colors for lineplot
    colors = ["black", "red", "blue", "green", "pink", "violet"]
    if indicator_name == "CO2 emissions (kt)":
        label = "kilo Tonns"
    elif indicator_name == "Urban population growth (annual %)":
        label = "Percentage (%)"
# driver code for plotting_data function
co2_data = data_plots(indicator_name="CO2 emissions (kt)")
data_plots(indicator_name="Urban population growth (annual %)")

def stats_plot():
    """This function plots the bar graph for the mean of the CO2 emission with the help of
    pandas statistical function mean()"""

    data_series = co2_data.mean(numeric_only=True)
    
    created_df = pd.DataFrame({"Years": years, "mean": data_series})
    created_df.set_index("Years").plot.bar(rot=0, title="Mean of CO2 emission" )

