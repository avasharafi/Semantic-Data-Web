import import_ipynb
import dash

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

from MainApp import app
from HelperFunctions import df
from HelperFunctions import start_table_df



# selected tab callback 
table_header = [
    html.Thead(html.Tr([html.Th("File"), html.Th("Query")]))
]
query1=html.Div("select * where {<http://de.dbpedia.org/resource/Karlsruhe> ?p ?o .}")
query2=html.Div([
    html.Div("select (COUNT(?person)  as ?cnt)  ?name where {"),
    html.Div("  ?person <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <"),
    html.Div("http://swrc.ontoware.org/ontology#Person> . "),
    html.Div("  ?person <http://swrc.ontoware.org/ontology#affiliation> ?aff ."),
    html.Div("  #  ?aff a <http://swrc.ontoware.org/ontology#affiliation>."),
    html.Div("  ?aff <http://swrc.ontoware.org/ontology#name> ?name ."),
    html.Div("} group by ?name")
])

row1 = html.Tr([html.Td(html.A("Karl.n3",href="../data/Karl.n3",download="Karl.n3")), html.Td(query1)])
row2 = html.Tr([html.Td(html.A("aifb_fixed_complete.nt",href="../data/aifb_fixed_complete.nt",download="aifb_fixed_complete.nt")), html.Td(query2)])

table_body = [html.Tbody([row1, row2])]

#render page for selected tab
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value'),
)
def render_content(tab):
    if tab == 'Dashboard':
        return html.Div([
            html.Div(id='output-data-upload'),
            html.Div(id='output-data-upload2'),
            html.Div([
                html.H3('Statistics'),
                html.Div(id='records-size',children=[]),
                html.Div(id='records-size2',children=[])
            ])
        ])
    elif tab == 'Tables':
        return html.Div([
            html.Div(
                id='MainTableDiv',
                children=[
                    dash_table.DataTable(
                        id='Resulttable',
                        style_table={'height': '250px', 'overflowY': 'auto'},
                        data=start_table_df.to_dict('records'), 
                        columns = [{'id': c, 'name': c} for c in start_table_df.columns],
                        style_cell=dict(textAlign='left'),   
                        editable=True,
                        filter_action="native",
                        sort_action="native",
                        sort_mode="multi",
                        column_selectable="single",
                        row_selectable="multi",
                        row_deletable=True,
                        selected_columns=[],
                        selected_rows=[],
                        page_action="native",
                        page_current= 0,
                        page_size= 10,
                        export_format="csv"
                    )
                ],
                style= {
                    'display': 'none',
                    'marginTop': '5px'
                }
            ),
            html.Div([
                 dbc.Alert(
                     ["There are no data for generating a table."],
                     id="alert-table",
                     is_open=False,
                     fade=True,
                     dismissable=True,
                     style={
                            'position': 'absolute',
                            'top': '20%', 
                            'right': '20%', 
                            'width': '40%',
                            'height': '5%',
                            'lineHeight': '20px',
                            'borderWidth': '1px',
                            'borderStyle': 'groove',
                            'margin': 'auto',
                            'fontSize': 'small',
                            'color': 'red',
                            'textAlign': 'center', 
                            },
                        

                 ),    
            ]),
            html.Div(
                id='MainTableDiv2',
                children=[
                    dash_table.DataTable(
                        id='Resulttable2',
                        style_table={'height': '250px', 'overflowY': 'auto'},
                        data=start_table_df.to_dict('records'), 
                        columns = [{'id': c, 'name': c} for c in start_table_df.columns],
                        style_cell=dict(textAlign='left'),   
                        editable=True,
                        filter_action="native",
                        sort_action="native",
                        sort_mode="multi",
                        column_selectable="single",
                        row_selectable="multi",
                        row_deletable=True,
                        selected_columns=[],
                        selected_rows=[],
                        page_action="native",
                        page_current= 0,
                        page_size= 10,
                        export_format="csv"
                    )
                ],
                style= {
                    'display': 'none',
                    'marginTop': '5px'
                }
            ),
            
            html.Div([
                 dbc.Alert(
                     ["There are no data for generating a table."],
                     id="alert-table2",
                     is_open=False,
                     dismissable=True,
                     style={
                            'position': 'absolute',
                            'top': '20%', 
                            'right': '20%', 
                            'width': '40%',
                            'height': '5%',
                            'lineHeight': '20px',
                            'borderWidth': '1px',
                            'borderStyle': 'groove',
                            'margin': 'auto',
                            'fontSize': 'small',
                            'color': 'red',
                            'textAlign': 'center'
                            },
                         
                    
                 ),    
                    ]),
            
        ])
    elif tab == 'Charts':
        return html.Div([
               html.Div(
                   id="result-graph",
                   className="result-graph",
                   children=[
                        dcc.Graph(
                            id='graph',
                            figure={
                                "layout": {
                                    "height": 500,
                                    'overflow': 'scroll'
                                },
                            },
                        ),
                
                     ],
                 style= {'display': 'none'}  
               ),

                html.Div([
                     dbc.Alert(
                         ["There are not enough data for generating the charts."],
                         id="alert-chart",
                         is_open=False,
                         fade=True,
                         dismissable=True,
                         style={
                            'position': 'absolute',
                            'top': '20%', 
                            'right': '20%', 
                            'width': '40%',
                            'height': '5%',
                            'lineHeight': '20px',
                            'borderWidth': '1px',
                            'borderStyle': 'groove',
                            'margin': 'auto',
                            'fontSize': 'small',
                            'color': 'red',
                            'textAlign': 'center'
                            },
                         
                        
                        
                     ),    
                 ]),
    
                html.Div(
                       id="result-graph2",
                       className="result-graph",
                       children=[
                            dcc.Graph(
                                id='graph2',
                                figure={
                                #"layout": {
                                #    "height": 270, 
                                #},
                            },
                            ),

                         ],
                     style= {'display': 'none'}  
                   ),

                html.Div([
                     dbc.Alert(
                         ["There are not enough data for generating the charts."],
                         id="alert-chart2",
                         is_open=False,
                         dismissable=True,
                         style={
                            'position': 'absolute',
                            'top': '20%', 
                            'right': '20%', 
                            'width': '40%',
                            'height': '5%',
                            'lineHeight': '20px',
                            'borderWidth': '1px',
                            'borderStyle': 'groove',
                            'margin': 'auto',
                            'fontSize': 'small',
                            'color': 'red',
                            'textAlign': 'center'
                            },
                         
                     )   
                 ]),

        ])
    elif tab == 'Maps':
        return html.Div([
               html.Div(
                   id="result-map",
                   className="result-map",
                   children=[
                        dcc.Graph(
                            id='map',
                            figure={
                                #"layout": {
                                 #   "height": 500, 
                                    
                                #},
                            },
                        ),                
                     ],
                 style= {'display': 'none'}  
               ),
               html.Div([
                    dbc.Alert(
                        ["\t"
                         "No coordinates have been found to display on the map.\n "
                         "You can choose latitude and longitude by dropdown menus."],
                        id="alert-map",
                        is_open=False,
                        fade=True,
                        dismissable=True,
                        style={
                                'position': 'absolute',
                                'top': '20%', 
                                'right': '20%', 
                                'width': '40%',
                                'height': '5%',
                                'lineHeight': '20px',
                                'borderWidth': '1px',
                                'borderStyle': 'groove',
                                'margin': 'auto',
                                'fontSize': 'small',
                                'color': 'orange',
                                'textAlign': 'center',
                                },
                         
                   
                    ),
               ]),
                
               html.Div([
                    dbc.Alert(
                    ["There are not enough data for generating a map. "],
                    id="alert-map3",
                    is_open=False,
                    fade=True,
                    dismissable=True,
                    style={
                            'position': 'absolute',
                            'top': '20%', 
                            'right': '20%', 
                            'width': '40%',
                            'height': '5%',
                            'lineHeight': '20px',
                            'borderWidth': '1px',
                            'borderStyle': 'groove',
                            'margin': 'auto',
                            'fontSize': 'small',
                            'color': 'red',
                            'textAlign': 'center',
                            },
                         
                    
                        )
               ]),            
               html.Div(
                   id="result-map2",
                   className="result-map",
                   children=[
                        dcc.Graph(
                            id='map2',
                            figure={
                                #"layout": {
                                #    "height": 500, 
                                #},
                            },
                        ),

                     ],
                 style= {'display': 'none'}  
               ),
               html.Div([
                    dbc.Alert(
                    ["No coordinates have been found to display on the map. \n" 
                     "You can choose latitude and longitude by dropdown menus."],
                    id="alert-map2",
                    is_open=False,
                    fade=True,
                    dismissable=True,
                    style={
                            'position': 'absolute',
                            'top': '20%', 
                            'right': '20%', 
                            'width': '40%',
                            'height': '5%',
                            'lineHeight': '20px',
                            'borderWidth': '1px',
                            'borderStyle': 'groove',
                            'margin': 'auto',
                            'fontSize': 'small',
                            'color': 'orange',
                            'textAlign': 'center',
                            },
                         
                    
                        )
               ]),
            html.Div([
                    dbc.Alert(
                    ["There are not enough data for generating a map. "],
                    id="alert-map4",
                    is_open=False,
                    fade=True,
                    dismissable=True,
                    style={
                            'position': 'absolute',
                            'top': '20%', 
                            'right': '20%', 
                            'width': '40%',
                            'height': '5%',
                            'lineHeight': '20px',
                            'borderWidth': '1px',
                            'borderStyle': 'groove',
                            'margin': 'auto',
                            'fontSize': 'small',
                            'color': 'red',
                            'textAlign': 'center'
                            },
                         
                    
                        )
               ])
            
        ])
    elif tab == 'Samples':
        return html.Div([
            html.Div(
                className="examples",
                children=[
                    dash_table.DataTable(
                        id='querySamples',
                        columns=[{"name": i, "id": i} for i in df.columns],
                        style_data_conditional=[
                            {
                                'if': {
                                    'state': 'active'  # 'active' | 'selected'
                                },
                                'backgroundColor': 'rgb(211, 224, 234)',
                                'border': '1px solid rgb(0, 116, 217)'
                            }
                        ],
                        data=df.to_dict('records'),
                        style_table={'width': '800px'},
                        style_cell=dict(textAlign='left'), 
                        column_selectable='single'
                    )
                ]),
                # dbc.Table(table_header + table_body, bordered=True,style={'fontSize':'small'}),
        ])
    elif tab == 'Tutorial':
        return html.Div([
            html.Div(
                className="tutorial",
                children=[
                    html.H3('Tutorial'),
                    
                    html.H4("- How to query an endpoint:"),
                    html.Div("First, write the query endpoint URL in the endpoint text area. Then type the query in the query text area and then press the SUBMIT button."),
                    
                    html.H4("- How to query an RDF file:"),
                    html.Div("Click on the upload area or simply drag the RDF file and drop it in the upload area and then write the query in query text area and finally press the SUBMIT button."),
                    
                    html.H4("- How to see the query result as a table:"),
                    html.Div("After submitting the query, go to the tables tab. You can see the query result there. you can also use the dropdowns to change the properties. Also you can export the table as a csv file by clicking on the export button."),

                    html.H4("- How to see the query result as a chart:"),
                    html.Div("After submitting the query, go to the charts tab to see the query result as a chart. Use the dropdowns to change the properties. You can also use the tools to zoom or export the chart as an image."),
                    
                    html.H4("- How to see the query result as a map:"),
                    html.Div("After submitting the query, go to the maps tab. You can see the result there. Use the tools on the top right for zoom and other functions. You can also use the dropdowns to change the properties."),

                    html.H4("- How to compare two queries:"),
                    html.Div("First, submit the first query either by querying an endpoint or uploading the RDF file. Then, open the compare text area by clicking on toggle compare box button. Then add the second query in one of the two possible ways described and press COMPARE button."),
                    
                    html.H4("- How to use query samples:"),
                    html.Div("In the query samples tab, you will find several samples. All you have to do is choosing one of them. The query will appear in the query text area and you can also see the endpoint in the endpoint text area. After clicking on SUBMIT button, you can see the query result in the table, chart or map tab."),
                ]),
        ])