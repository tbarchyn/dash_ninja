# Dash lineplot - simple lineplots of pandas frames
# 22 Sept 2017
# Tom Barchyn
# This is mostly copied from the dash documentation (credit goes to them)

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from dash_lineplot_functions import *
from dash_lineplot_updater import *

app = dash.Dash ()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# app layout
app.layout = html.Div([
    html.Div([
        html.Label ('seconds to display backwards in time (s):  '),
        dcc.Input (type = 'text', id = 'display_interval', value = '60'),
        dcc.RadioItems(
            id = 'auto_update',
            options=[
                {'label': 'automatically update', 'value': 'auto_update'},
                {'label': 'stop automatically updating', 'value': 'no_auto_update'},
            ],
            value='auto_update'
        ),
        dropdown_prototype ('columns1', df),
        dcc.Graph (id = 'plot1'),
        dropdown_prototype ('columns2', df),
        dcc.Graph (id = 'plot2'),
        dcc.Interval (
            id= 'interval-component',
            interval = 1 * 1000
        )
    ])
])

# first plot
@app.callback(
    output = dash.dependencies.Output ('plot1', 'figure'),
    inputs = [dash.dependencies.Input ('columns1', 'value'),
              dash.dependencies.Input ('display_interval', 'value'),
              dash.dependencies.Input ('auto_update', 'value')],
    events = [dash.dependencies.Event ('interval-component', 'interval')])
def update_plot1 (column_names, display_interval, auto_update):
    return (lineplot (df, column_names, display_interval, auto_update))

# second plot
@app.callback(
    output = dash.dependencies.Output ('plot2', 'figure'),
    inputs = [dash.dependencies.Input ('columns2', 'value'),
              dash.dependencies.Input ('display_interval', 'value'),
              dash.dependencies.Input ('auto_update', 'value')],
    events = [dash.dependencies.Event ('interval-component', 'interval')])
def update_plot2 (column_names, display_interval, auto_update):
    return (lineplot (df, column_names, display_interval, auto_update))



if __name__ == '__main__':
    # read in the dataframe and get the headers
    df = pd.read_csv ('../sub.csv')    
    headers = df.columns
    df = df.ix[0:10, :]                 # cut to the first part

    # start up the updater
    updater = dash_updater (df, {'filename': '../sub.csv', 'update_interval': 1.0})
    updater.start ()
    
    app.run_server ()
    