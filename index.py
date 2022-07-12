from app import app

from tabs.tab_animalsMeters import animalsMetersLayout
from tabs.tab_animalsFeet import animalsFeetLayout


from dash import html, dcc



app.layout = html.Div(children=[


        dcc.Tabs([                 
                    animalsMetersLayout(),
                    animalsFeetLayout()



            ])    
        ])


if __name__ == '__main__':
        app.run_server(port='8080',debug=True)
