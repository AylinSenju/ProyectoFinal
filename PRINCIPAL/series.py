import dash
import pandas as pd
from click import style
from dash import dcc, html, Dash, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc


data = pd.read_csv("DATA/Df_Series_Limpio")

def mejores(data):
    datas = data.sort_values(by="calificacion", ascending=False)
    data_top = datas.head(10)
    fig = px.bar(data_top, x="nombre", y="calificacion",
                 title="Ranking de Series",
                 labels={"nombre": "Series", "calificación": "Calificación"})

    fig.update_layout(
        xaxis_title="Nombre de la Serie",
        yaxis_title="Calificación",
        template="seaborn"
    )

    fig.update_traces(marker_color="#f9d659")
    return fig

def peores(data):
    datas = data.sort_values(by="calificacion", ascending=True)
    data_top = datas.head(10)
    fig = px.bar(data_top, x="nombre", y="calificacion",
                 title="Ranking de Series",
                 labels={"nombre": "Series", "calificación": "Calificación"})

    fig.update_layout(
        xaxis_title="Nombre de la Serie",
        yaxis_title="Calificación",
        template="seaborn"
    )

    fig.update_traces(marker_color="#f9d659")
    return fig


def genero(data):
    genero_promedio = data.groupby("genero")["calificacion"].mean().reset_index()

    fig = px.pie(genero_promedio, values="calificacion", names="genero",
                 title="Ranking Promedio por Género")

    return fig


def dashboard():
    fig1 = mejores(data)
    fig2 = peores(data)
    fig3 = genero(data)

    body = html.Div([
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H4("Selecciona una grafica:", style={"color": "#f5c518"}),
                        html.Hr(),
                        dcc.Dropdown(
                            id="graph-dropdown",
                            options=[
                                {"label": "Mejores Series", "value": "mejores"},
                                {"label": "Peores Series", "value": "peores"},
                                {"label": "Promedio por Género", "value": "genero"}
                            ],
                            value="mejores",
                            style={"width": "50%", "color":"yellow", "padding": "3px", "backgroundColor": "#FFFFFF"}
                        ),
                        html.Div(id="graph-container")
                    ], style={"backgroundColor": "#FFFFFF"})
                )
            ]
        ),
    ])

    return body

@callback(Output("graph-container", "children"),[Input("graph-dropdown", "value")])
def update_grafica(selected_graph):
    if selected_graph == "mejores":
        return dcc.Graph(figure=mejores(data), style={"backgroundColor": "#FFFFFF"})
    elif selected_graph == "peores":
        return dcc.Graph(figure=peores(data), style={"backgroundColor": "#FFFFFF"})
    elif selected_graph == "genero":
        return dcc.Graph(figure=genero(data), style={"backgroundColor": "#FFFFFF"})
    return html.Div()

if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = dashboard()
    app.run(debug=True)


