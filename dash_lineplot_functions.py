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

def dropdown_prototype (id_name, df):
    '''
    method to make dropdown prototype
    id_name = the html id
    df = the pandas dataframe
    '''
    return (
    html.Div([
        dcc.Dropdown(
            id = id_name,
            options = [{'label': i, 'value': i} for i in df.columns],
            value = '',
            multi = True
            ),
        ], 
        style={'width': '100%', 'display': 'inline-block'})
    )

def lineplot (df, column_names, lookback):
    '''
    method to return a plot
    '''
    max_x_display = df['log_time'].max ()
    min_x_display = max_x_display - lookback
    
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
                'range': [min_x_display, max_x_display],
                'showgrid': True,
                'rangeslider': dict ()
            },
            yaxis = {
                'title': 'Value',
                'showgrid': True,
            },
            margin = {'l': 40, 'b': 40, 't': 10, 'r': 0},
            legend = {'x': 0, 'y': 1},
            hovermode = 'closest'
        )
    }


def update_df (df):
    '''
    method to update the dataframe
    df = the dataframe
    '''
    
    
    return (df)

