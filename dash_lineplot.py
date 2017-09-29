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

app = dash.Dash ()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# read in the dataframe and get the headers
df = pd.read_csv ('../sub.csv')    
headers = df.columns

# app layout
app.layout = html.Div([
    html.Div([
        html.Label ('Seconds to display (s):  '),
        dcc.Input (type = 'text', id = 'display_interval', value = '60'),
        html.Button ('Pause updates', id = 'pause'),
        html.Button ('Resume updates', id = 'resume'),
        dropdown_prototype ('columns1', df),
        dcc.Graph (id = 'plot'),
    ])
])

@app.callback(
    dash.dependencies.Output('plot', 'figure'),
    [dash.dependencies.Input('columns1', 'value')])
def update_graph (column_names):
    '''
    callback to update the graph
    '''
    return {
        'data': [
            go.Scatter(
                x = df ['log_time'],
                y = df [column_name],
                name = column_name
            ) for column_name in column_names
        ],
        'layout': go.Layout(
            xaxis = {
                'title': 'Log time (s)',
                'rangeslider': dict ()
            },
            yaxis = {
                'title': 'Value',
            },
            margin = {'l': 40, 'b': 40, 't': 10, 'r': 0},
            legend = {'x': 0, 'y': 1},
            hovermode = 'closest'
        )
    }

if __name__ == '__main__':
    app.run_server ()
    
    