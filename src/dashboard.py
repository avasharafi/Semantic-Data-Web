import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div([
    html.Div(
        className="navbar",
        children=[
            html.H3('Interactive Data Analytics Dashboard for RDF Knowledge Graphs', className="navbar--title"),
            html.Div(
                className="navbar--btns",
                children=[
                    html.Span(
                        className="navbar--btn_left",
                        children="Dashboard"
                    ),
                    html.Span(
                        className="navbar--btn_left",
                        children="Tables"
                    ),
                    html.Span(
                        className="navbar--btn_left",
                        children="Charts"
                    ),
                    html.Span(
                        className="navbar--btn_left",
                        children="Query Samples"
                    ),
                    html.Span(
                        className="navbar--btn_right",
                        children="Upload"
                    ),
                    html.Span(
                        className="navbar--btn_right",
                        children="Download"
                    ),
                ]
             )
        ]
    ),
    html.Div(
        className="querybox",
        children=[
            html.H4("SPARQL Query", className="querybox--title"),
            html.Textarea(className="querybox--textarea"),
            html.Button("SUBMIT", className="querybox--btn")
        ]
    ),
    # dcc.Graph(
    #     id='Graph1',
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montreal'},
    #         ],
    #         'layout': {
    #             'plot_bgcolor': colors['background'],
    #             'paper_bgcolor': colors['background'],
    #             'font': {
    #                 'color': colors['text']
    #             }
    #         }
    #     }
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)
