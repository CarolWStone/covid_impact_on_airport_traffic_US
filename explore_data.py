import pandas as pd
import os
import re
import pdb

USA_COUNTRY = 'United States of America (the)'
BY_AIRPORT_DIR = 'dataframes_by_airport'
def find_all_usa_statistics():
    # step one: initial parsing: find data regarding USA airports. write to file and drop unecessary columns
    df = pd.read_csv("covid_impact_on_airport_traffic.csv")
    print(df.columns)
    print(df.head(10))
    print(df['Country'].unique())

    american_aviation = df.loc[df['Country'] == USA_COUNTRY]
    print(f'Number of USA rows: {len(american_aviation)}')
    print('Distinct American airports')
    print(american_aviation['AirportName'].unique())
    american_aviation.drop(columns=['ISO_3166_2', 'Centroid', 'Geography'], inplace=True)
    american_aviation.to_csv("covid_impact_usa_traffic.csv", index=False)

def find_statistics_by_airport():
    # step two: unique dataframes for each airport:
    if not os.path.exists("dataframes_by_airport"):
        os.makedirs("dataframes_by_airport")
    
    df = pd.read_csv("covid_impact_usa_traffic.csv")
    airport_names = df['AirportName'].unique()
    for airport in airport_names:
        airport_df = df.loc[df['AirportName'] == airport]
        airport_file_pointer = re.sub("[\/ ]", "_", airport).lower()
        airport_df.to_csv(BY_AIRPORT_DIR + f"/{airport_file_pointer}.csv", index=False)


# find_all_usa_statistics()
find_statistics_by_airport()
