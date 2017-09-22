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

app = dash.Dash ()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

df = pd.read_csv ('../sub.csv')    
headers = df.columns

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id = 'columns',
                options = [{'label': i, 'value': i} for i in df.columns],
                value = '',
                multi = True
            ),
        ],
        style={'width': '100%', 'display': 'inline-block'}),
    
    dcc.RangeSlider (
        id = 'time_slider',
        min = df['log_time'].min (),
        max = df['log_time'].max (),
        step = 1,
        value = [df['log_time'].min (), df['log_time'].max ()]
    ), 

    dcc.Graph (id = 'plot'),
    ])
])

@app.callback(
    dash.dependencies.Output('plot', 'figure'),
    [dash.dependencies.Input('columns', 'value'),
     dash.dependencies.Input('time_slider', 'value')])
def update_graph (column_names, time_range):
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
                'range': [time_range[0], time_range[1]]
            },
            yaxis = {
                'title': 'Value'
            },
            margin = {'l': 40, 'b': 40, 't': 10, 'r': 0},
            legend = {'x': 0, 'y': 1},
            hovermode = 'closest'
        )
    }

if __name__ == '__main__':
    app.run_server ()
    
    