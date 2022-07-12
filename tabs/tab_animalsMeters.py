from app import app
from components import components
from usefulFunctions import usefulFunctions

import dash
from dash.dependencies import Input, Output, State
from dash import dcc
import plotly.express as px
import pandas as pd



def animalsMetersLayout():

    #*********************************************************************************************************************************
    # Create Dropdown
    #*********************************************************************************************************************************

        @app.callback(Output('dropdown_animalsMetersDiv','children'),
                        [Input('animalsMetersDivHidden','children')])
        def dropMyFirstTab(divHidden):    

                df = df = usefulFunctions.loadCSV('tallAnimals.csv')
                animals = list(df.Animal.unique())

                options = [{'label':i, 'value':i} for i in animals]
                values = animals

                return components('dropdown_animalsMeters').Dropdown(options,values)




    #*********************************************************************************************************************************
    # Create Bar Chart
    #*********************************************************************************************************************************
        @app.callback(Output('barchart_animalsMetersDiv','children'),
                        [Input('dropdown_animalsMeters','value')])
        def barMyFirstTab(dropValues):   

                df = df = usefulFunctions.loadCSV('tallAnimals.csv')
                df = df.query("Animal.isin(@dropValues)")

                return components('barchart_animalsMeter').barChart(data=df,x='Animal',y='Meters',labels={'Meters':'Meters','Animal':''})



           
                
       


    #*********************************************************************************************************************************
    # Layout
    #*********************************************************************************************************************************
        layout =  dcc.Tab(label = 'Animal Height in Meters',children = [

                                        components('dropdown_animalsMetersDiv').componentDiv(),

                                        components('barchart_animalsMetersDiv').componentDiv(),

                                        components('animalsMetersDivHidden').componentDiv()


                        ],className='w-25')



        return layout