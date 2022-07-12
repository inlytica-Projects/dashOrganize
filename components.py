from dash import Dash, html, dash_table, dcc
import plotly.express as px




colorDict = {
        'backgroundColor':'#303030', #bootswatchDarkly  --bs-dark
        'fontColor':'#fff',  #bootswatchDarkly  --bs-white
        'primaryMarkerColor': '#375a7f' #bootswatchDarkly --bs-primary
                }

                

class components:




        def __init__(self,componentId):
                self.componentId = componentId

        
        # Div___________________________________________________________________________________________________________________________________
        def componentDiv(self):
                return html.Div(id=self.componentId, 
                                style={'margin-top':0,'margin-bottom':0,'margin-left':0,'margin-right':0}
                                )



        # Dropdown_______________________________________________________________________________________________________________________________
        def Dropdown(self,options,value):
                return dcc.Dropdown(options = options, value = value, multi=True, id=self.componentId)



        # Bar Chart_______________________________________________________________________________________________________________________________
        def barChart(self, data, x, y,**optionalArgs):   


                # Optional arguments
                orientation=optionalArgs.get('orientation')
                color = optionalArgs.get('color')
                barmode = optionalArgs.get('barmode')
                hover_data = optionalArgs.get('hover_data',[])
                labels = optionalArgs.get('labels',{})

                fig = px.bar(data, y=y, x=x, orientation=orientation, 
                                color = color,
                                barmode=barmode,
                                hover_data = hover_data,
                                labels = labels)

                fig.update_layout(margin=dict(l=0, r=0, b=0, pad=0),
                plot_bgcolor = colorDict['backgroundColor'],
                paper_bgcolor= colorDict['backgroundColor'],
                font_color=colorDict['fontColor'],
                title={
                        

                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'}

                )
                
                fig.update_traces(marker_color=colorDict['primaryMarkerColor'])  




                return dcc.Graph(id=self.componentId,figure = fig)



        # DataTable_______________________________________________________________________________________________________________________________
        def dataTable(self,columns,data,editable=False,**optionalArgs):

                return  dash_table.DataTable(id=self.componentId,

                        columns = columns,
                        data = data,
                        editable = editable,

                        # Optional arguments
                        tooltip_data = optionalArgs.get('tooltip_data',[]),


                        style_data={
                                'backgroundColor': colorDict['backgroundColor'],
                                'color': colorDict['fontColor']
                                },
                

                        style_data_conditional=[                
                                {
                                "if": {"state": "selected"},            

                                "border": "2px solid #00bc8c",
                                'color':'#fff'
                                },
                                ],

                        style_table={'overflowX':'scroll'},
                        style_cell = {
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                                'maxWidth': 0
                        },

                        tooltip_duration=None,
                        sort_action='custom',
                        sort_mode='multi',
                        sort_by=[],
                        filter_action='custom',
                        filter_query=''


                        )