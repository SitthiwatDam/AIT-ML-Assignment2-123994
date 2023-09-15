
# Import packages
from dash import Dash, html, callback, Output, Input, State, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import pickle
import numpy as np

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.LUX]
new_model = Dash(__name__, external_stylesheets=external_stylesheets)

# load the model from disk
loaded_model = pickle.load(open('./model/model.pkl', 'rb'))
loaded_encoder = pickle.load(open('./model/label_encoderA2.model', 'rb'))
loaded_scaler = pickle.load(open('./model/minmax_scalerA2.model', 'rb'))


# App layout
new_model.layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.Br(),
            
            html.Label("-------Car's price prediction (New-Version)-------",  style={"font-size": "50px", "font-weight": "Bold", "vertical-align" : "center",'color':'green'}),
            html.Br(),
            html.Label("With our newer version of the machine learning model (LinearRegression) that we build from scratch, the predicted result can calculated more precisely...?"
                    ,  style={"font-size": "20px", "vertical-align" : "center",'color':'black'}),
            html.Br(),
                html.Label("Let's predict your car prices!"
                        ,  style={"font-size": "20px", "vertical-align" : "center",'color':'black'}),
            html.Br(),
             html.Br(),
            dbc.Label("Type the max power of the car.",  style={"font-size": "25px"}),
            dbc.Input(id="mp_new", type="number", placeholder="Put a value for max power", size="lg"),
            html.Br(),
            dbc.Label("Type the year of the car.", style={"font-size": "25px", 'text-align' : 'middle'}),
            dbc.Input(id="year_new", type="number", placeholder="Put a value for year", size="lg"),
            html.Br(),
            dbc.Label("Please select the type of fuel.", style={"font-size": "25px"}),
            dbc.Select(id='selected_fuel_new', size="lg", options=[
                {"label": "Diesel", "value": "Diesel"},
                {"label": "Petrol", "value": "Petrol"},],
            ),
            
            html.Br(),
            html.Button(id="submit_new", children="price_prediction", className="btn btn-outline-primary"), 
            html.Br(),
            html.Br(),
            dbc.Card([
                    dbc.CardHeader("Predicted price (Baht)",style={"font-size": "30px", "font-weight": "700", "color":"black"}),
                    dbc.CardBody(html.Output(id="y_new",style={"font-size": "30px", "font-weight": "700", "color":"black"}))
                    ],style={   
                                "display": "flex",
                                "justify-content": "center",  
                                "align-items": "center",      
                                "width": "500px",             
                                "margin": "auto",           
                            }, color="success", inverse=True)
            
        ],
        className="mb-3")
    ],justify='center')

], fluid=True)


@callback(
    Output(component_id="y_new", component_property="children"),
    State(component_id="mp_new", component_property="value"),
    State(component_id="year_new", component_property="value"),
    State(component_id="selected_fuel_new",component_property='value'),
    Input(component_id="submit_new", component_property='n_clicks'),
    prevent_initial_call=True
)



def price_prediction(mp_new,year_new,selected_fuel_new,submit_new):
    
    #Scale features: 'max_power','year'
    sample = pd.DataFrame([[float(mp_new),float(year_new), str(selected_fuel_new)]],columns=['max_power','year','fuel'])
    sample[['max_power','year']]  = loaded_scaler.transform(sample[['max_power','year']])
    
    #Lable encoding 'fuel' before prediction
    sample['fuel'] = loaded_encoder.transform(sample['fuel'])
    
    #Predicted the price by loading model that we saved
    predicted_exp = loaded_model.predict(sample)
    
    return  dbc.Col(dbc.Card(np.exp(predicted_exp)  , color="success", inverse=True))

