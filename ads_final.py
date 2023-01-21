#!/usr/bin/env python
# coding: utf-8

# In[31]:


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

    # filter the dataframe with given countries and indicator name and set the index as Country Name.
    selected_data = df[(df["Country Code"].isin(country_codes)) & (df["Indicator Name"] == indicator_name)].set_index("Country Code")

    # filter the dataframe with given years and reset the index
    filtered_data = selected_data.loc[:, years]
    filtered_data_T = selected_data.loc[:, years].transpose()
    filtered_data_T.plot(kind = "line",linestyle="--", marker="o",ylabel=label, title=indicator_name)
 
    plt.legend(bbox_to_anchor=(1.0, 1.0))
    return filtered_data
    
# driver code for plotting_data function
co2_data = data_plots(indicator_name="CO2 emissions (kt)")
data_plots(indicator_name="Urban population growth (annual %)")

def stats_plot():
    """This function plots the bar graph for the mean of the CO2 emission with the help of
    pandas statistical function mean()"""

    data_series = co2_data.mean(numeric_only=True)
    
    created_df = pd.DataFrame({"Years": years, "mean": data_series})
    created_df.set_index("Years").plot.bar(rot=0, title="Mean of CO2 emission" )



# driver code for mean_stats function
stats_plot()


def correlation_plots(country_name):
    """This function takes the Country Name as argument and cross compare
    the correlations between different indicators of the Country and plot the heatmap"""

    # filter the dataframe with given country name
    country_data =df[df["Country Name"]==country_name].set_index("Indicator Name")

    # extract the data for the given years and indicator names and transpose the dataframe
    corr_data = country_data.loc[indicator_names, years].transpose()
    
    # plot the heatmap for the correlation between different indicators
    plt.title(country_name)
    sns.heatmap(corr_data.corr(), linecolor='white',
                linewidths=0.1, annot=True, cmap="PuOr")
    return corr_data


correlation_plots("Bangladesh")
correlation_plots("Russian Federation")

