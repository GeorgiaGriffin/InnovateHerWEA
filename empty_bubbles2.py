#ALMOST functional- missing dataframe w lat, long, SA

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

#load country codes
country_codes = px.data.gapminder().iloc[:, [0, 3, 4]].drop_duplicates()
#.iloc[:, [0, -1]].drop_duplicates()
"""country_data = pd.read_csv("C:/Users/tgowe/Desktop/IH/country_data0.csv")
state_data = pd.read_csv("C:/Users/tgowe/Desktop/IH/state_data.csv")"""

# data upload and parsing
locs = {"class":[], "v_area":[], "country":[], "date":[], "country_name":[], "latitude":[], "longitude":[], "area":[]}
loc = open("C:/Users/tgowe/Desktop/IH/loc.txt", "r")
for line in loc:
    # Split each line into longitude and latitude using a delimiter (e.g., comma)
    values = line.strip().split(',')
        
    # Append the values to the respective lists in the dictionary
    locs["class"].append(str(values[0]))
    locs["v_area"].append(int(values[1]))
    locs["country"].append(str(values[2]))
    locs["date"].append(int(values[3]))
    locs["country_name"].append(str(values[4]))
    locs["latitude"].append(np.nan)
    locs["longitude"].append(np.nan)
    locs["area"].append(np.nan)

loc.close()

#generate dataframe
df = pd.DataFrame(locs)

print(country_codes)
merged_df = pd.merge(df, country_codes, left_on="country", right_on="country", how="left")

fig = px.scatter_geo(merged_df, lat="latitude", lon="longitude", color="class", hover_name="country_name", size="v_area", projection="natural earth", animation_frame="date")

#generates graph
#fig = px.scatter_geo(df, locations="country", color="class", hover_name="name", size="area", projection="natural earth")
fig.show()
