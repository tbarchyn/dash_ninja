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

def scatterplot (df, column_name, auto_update):
    '''
    method to return a scatterplot
    df = the dataframe
    column_name = the column name to plot
    auto_update = the auto_update variable
    '''
    if auto_update == 'auto_update':
        # return vanilla scatterplot
        return {
            'data': [
                go.Scatter(
                    x = df ['x_utm'],
                    y = df ['y_utm'],
                    name = column_name,
                    mode = 'marker'
                )
            ],
            'layout': go.Layout(
                xaxis = {
                    'title': 'x utm (m)',
                    'showgrid': True,
                },
                yaxis = {
                    'title': 'y utm (m)',
                    'showgrid': True,
                },
                margin = {'l': 40, 'b': 40, 't': 10, 'r': 0},
                legend = {'x': 0, 'y': 1},
                hovermode = 'closest',
            )
        }
    
    else:
        pass                # don't do anything!


def lineplot (df, column_names, display_interval, auto_update):
    '''
    method to return a plot
    df = the dataframe
    column_names = the column names to plot
    display_interval = the display interval in seconds
    auto_update = the auto_update variable
    '''
    if auto_update == 'auto_update':
        # try to parse the display interval
        try:
            display_interval = float (display_interval)
        except:
            display_interval = 60.0         # just use default
        
        # set up the interval
        max_x_display = df['log_time'].max ()
        min_x_display = max_x_display - display_interval
        
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
    
    else:
        pass                # don't do anything!

    
    