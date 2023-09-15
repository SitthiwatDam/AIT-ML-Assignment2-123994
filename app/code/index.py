from dash import Dash, html, callback, Output, Input, State, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import pickle
import numpy as np
from old_model import old_model
from new_model import new_model

external_stylesheets = [dbc.themes.LUX]
app = Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

# Define the layout for the Main Page
main_layout = html.Div([
    
    dbc.NavbarSimple(
        children=[
            
            dbc.NavItem(dbc.NavLink("New Model", href="/new_model")),
            dbc.NavItem(dbc.NavLink("Old Model", href="/old_model")),
        ],
        brand="Chacky Company Co., Ltd.",
        brand_href="/",
        color="primary",
        dark=True,
    ),
    
    html.Div(id="page-content")
],
    style={"text-align": "center"})

# Set up URL routing
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    main_layout
],
    style={"text-align": "center"})

intro_layout=  html.Div([
    
    html.Label('CHACKY COMPANY CO., LTD.', style={'textAlign': 'center', 'fontSize': 80, 'marginTop': '40vh', 'transform': 'translateY(-50%)',"font-weight": "1000"}),
    html.Br(),
    html.Label( ' You are now entering: Car\'s Price Prediction site', style={'textAlign': 'center', 'fontSize': 40,"font-weight": "400"}),
    html.Br(),
    html.Label( 'Please select the predicted model at the top right of the page', style={'textAlign': 'center', 'fontSize': 20,"font-weight": "200"})
])
# Callback to update page content based on the URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/new_model":
        return new_model.layout
    elif pathname == "/old_model":
        return old_model.layout
    elif pathname == "/":
        return intro_layout




if __name__ == "__main__":
    app.run_server(debug=True)
