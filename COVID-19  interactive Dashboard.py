
# coding: utf-8

# In[7]:


import numpy as np 
import pandas as pd 
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


# In[17]:


df = pd.read_csv("C:/Users/shahh/Downloads/novel-corona-virus-2019-dataset/covid_19_data.csv")
df


# In[20]:


df = df.rename(columns={'Country/Region':'Country'})
df = df.rename(columns={'ObservationDate':'Date'})


# In[36]:


df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
df_countries = df_countries.drop_duplicates(subset = ['Country'])
df_countries = df_countries[df_countries['Confirmed']>0]
df_countries = df_countries[df_countries['Deaths']>0]
df_countries = df_countries[df_countries['Recovered']>0]


df_countries


# In[66]:


for col in df_countries.columns:
    df_countries[col] = df_countries[col].astype(str)

df_countries['text'] ='Country : ' + df_countries['Country'] + '<br>' + 'Recovered : ' + df_countries['Recovered'] +  '<br>' + 'Deaths : ' + df_countries['Deaths'] 


fig = go.Figure(data=go.Choropleth(
    locations = df_countries['Country'],
    locationmode = 'country names',
    z =df_countries['Confirmed'],
    colorscale = 'Blues',
    marker_line_color = 'black',
    marker_line_width = 0.5,
    text=df_countries['text'],
))

fig.update_layout(
    title_text = 'Confirmed Cases all around the world',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
        projection_type = 'natural earth'
    )
)

