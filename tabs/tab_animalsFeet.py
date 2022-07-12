from app import app
from components import components
from usefulFunctions import usefulFunctions


import dash
from dash.dependencies import Input, Output, State
from dash import dcc
import plotly.express as px
import pandas as pd

def animalsFeetLayout():

    #*********************************************************************************************************************************
    # Create Dropdown
    #*********************************************************************************************************************************

        @app.callback(Output('dropdown_animalsFeetDiv','children'),
                        [Input('animalsFeetDivHidden','children')])
        def dropMyFirstTab(divHidden):    

                df = usefulFunctions.loadCSV('tallAnimals.csv')  
                animals = list(df.Animal.unique())

                options = [{'label':i, 'value':i} for i in animals]
                values = animals

                return components('dropdown_animalsFeet').Dropdown(options,values)




    #*********************************************************************************************************************************
    # Create Bar Chart
    #*********************************************************************************************************************************
        @app.callback(Output('barchart_animalsFeetDiv','children'),
                        [Input('dropdown_animalsFeet','value')])
        def barMyFirstTab(dropValues):   

                df = usefulFunctions.loadCSV('tallAnimals.csv') 
                df = df.query("Animal.isin(@dropValues)")

                return components('barchart_animalsFeet').barChart(data=df,x='Animal',y='Feet',labels={'Meters':'Meters','Animal':''})



           
                
       


    #*********************************************************************************************************************************
    # Layout
    #*********************************************************************************************************************************
        layout =  dcc.Tab(label = 'Animal Height in Feet',children = [

                                        components('dropdown_animalsFeetDiv').componentDiv(),

                                        components('barchart_animalsFeetDiv').componentDiv(),

                                        components('animalsFeetDivHidden').componentDiv()


                        ],className='w-25')



        return layout