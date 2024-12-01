import dash
import pandas as pd
from dash import dcc, html, Dash, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc


data = pd.read_csv("data/Df_Peliculas_Limpio")

data["estreno"] = pd.to_datetime(data["estreno"], errors="coerce")

data["mes_estreno"] = data["estreno"].dt.month

def distribucion_estrenos_por_mes(data):
    fig = px.histogram(data, x="mes_estreno", nbins=12,
                       title="Distribución de Estrenos por Mes",
                       labels={"mes_estreno": "Mes de Estreno"},
                       category_orders={
                           'mes_estreno': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                       })

    fig.update_layout(
        xaxis_title="Mes de Estreno",
        yaxis_title="Número de Películas",
        template="plotly_dark",
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(1, 13)),
            ticktext=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                      "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        )
    )
    fig.update_traces(marker_color='#f5c518')
    return fig

def test():
    fig_dist_estrenos = distribucion_estrenos_por_mes(data)

    body = html.Div([
        html.H3("Distribución de Estrenos por Mes", style={"color":"#FFFFFF"}),
        html.P("Análisis de la distribución de estrenos en diferentes meses del año", style={"color":"#FFFFFF"}),

        dcc.Dropdown(
            options=[
                {"label": "2021", "value": 2021},
                {"label": "2022", "value": 2022},
                {"label": "2023", "value": 2023},
            ],
            value="2023",
            id="ddAño"
        ),
        html.Hr(),
        dcc.Graph(figure=fig_dist_estrenos, id="figDistEstrenos")
    ],
    style={
        "background-color": "#000000"
    })

    return body

@callback(
    Output(component_id="figDistEstrenos", component_property="figure"),
    Input(component_id="ddAño", component_property="value")
)
def update_grafica(value_año):
    if value_año == "all":
        filtered_data = data
    else:
        filtered_data = data[data["estreno"].dt.year == value_año]

    fig_dist_estrenos = distribucion_estrenos_por_mes(filtered_data)

    return fig_dist_estrenos
