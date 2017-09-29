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



def update_df (df):
    '''
    method to update the dataframe
    df = the dataframe
    '''
    
    
    return (df)

