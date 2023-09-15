# Import packages
from dash import Dash, html, callback, Output, Input, State, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import pickle
import numpy as np

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.LUX]
old_model = Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

# load the model from disk
loaded_model = pickle.load(open('./model/selling_price.model', 'rb'))
loaded_encoder = pickle.load(open('./model/label_encoder.model', 'rb'))
loaded_scaler = pickle.load(open('./model/standard_scaler.model', 'rb'))


# App layout
old_model.layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.Br(),
            html.Label("-------Car's price prediction (Old-Version)-------",  style={"font-size": "50px", "font-weight": "800", "vertical-align" : "center", 'color': 'red'}),
            html.Br(),
            html.Label("This is the older version of company's machine learning model (RandomForest)"
                    ,  style={"font-size": "20px", "vertical-align" : "center",'color':'black'}),
            html.Br(),
            html.Br(),
            dbc.Label("Type the max power of the car.",  style={"font-size": "25px"}),
            dbc.Input(id="mp", type="number", placeholder="Put a value for max power", size="lg"),
            html.Br(),
            dbc.Label("Type the year of the car.", style={"font-size": "25px", 'text-align' : 'middle'}),
            dbc.Input(id="year", type="number", placeholder="Put a value for year", size="lg"),
            html.Br(),
            dbc.Label("Please select the type of fuel.", style={"font-size": "25px"}),
            dbc.Select(id='selected_fuel', size="lg", options=[
                {"label": "Diesel", "value": "Diesel"},
                {"label": "Petrol", "value": "Petrol"},],
            ),
            
            html.Br(),
            html.Button(id="submit", children="price_prediction", className="btn btn-outline-primary"), 
            html.Br(),
            html.Br(),
                dbc.Card([
                    dbc.CardHeader("Predicted price (Baht)",style={"font-size": "30px", "font-weight": "700", "color":"black"}),
                    dbc.CardBody(html.Output(id="y",style={"font-size": "30px", "font-weight": "700", "color":"black"}))
                    ],style={   
                                "display": "flex",
                                "justify-content": "center",  # Center horizontally
                                "align-items": "center",      # Center vertically
                                "width": "500px",             # Set a fixed width
                                "margin": "auto",            # Center horizontally within the parent container
                            }, color="warning", inverse=True)
                                    
        ],
        className="mb-3")
    ],justify='center')

],
    style={"text-align": "center"}, fluid=True)


@callback(
    Output(component_id="y", component_property="children"),
    State(component_id="mp", component_property="value"),
    State(component_id="year", component_property="value"),
    State(component_id="selected_fuel",component_property='value'),
    Input(component_id="submit", component_property='n_clicks'),
    prevent_initial_call=True
)



def price_prediction(mp,year,selected_fuel,submit):
    
    #Scale features: 'max_power','year'
    sample = pd.DataFrame([[float(mp),float(year), str(selected_fuel)]],columns=['max_power','year','fuel'])
    sample[['max_power','year']]  = loaded_scaler.transform(sample[['max_power','year']])
    
    #Lable encoding 'fuel' before prediction
    sample['fuel'] = loaded_encoder.transform(sample['fuel'])
    
    #Predicted the price by loading model that we saved
    predicted_exp = loaded_model.predict(sample)
    result = np.exp(predicted_exp)
    return  dbc.Col(dbc.Card(result  , color="success", inverse=True))
