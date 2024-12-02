import dash
import pandas as pd
from dash import dcc, html, Dash, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc


data = pd.read_csv("data/Df_Peliculas_Limpio")

data["estreno"] = pd.to_datetime(data["estreno"], errors="coerce")
data["duracion_min"] = data["duracion"].str.extract(r"(\d+)").astype(float)


def distribucion_calificaciones(data):
    fig = px.histogram(data, x="calificacion", nbins=10,
                       labels={"calificacion": "Calificación"},
                       text_auto=True)

    fig.update_layout(
        xaxis_title="Calificación",
        yaxis_title="Número de Películas",
        template="plotly_dark",
        bargap=0.2
    )
    fig.update_traces(marker_color='#f5c518')
    return fig

#ANTES ERA LA CUATROOO
def distribucion_generos(data):
    generos= data["genero"].value_counts().reset_index()
    generos.columns=["genero", "cantidad"]

    fig_dos=px.pie(
        generos,
        names="genero",
        values="cantidad",
        color="genero",
        template="plotly_dark"
    )
    return fig_dos


def estrenos_fecha(data):
    agrupado = data.groupby("estreno",as_index=False).size()
    fig_tres=px.line(agrupado,
                     x="estreno", y="size",
                     labels={"estreno":"Fecha Estreno", "size":"Cantidad de Peliculas"})
    fig_tres.update_layout(
        xaxis_title="Fecha de Estreno",
        yaxis_title="Cantidad de Peliculas",
        template="plotly_dark"
    )
    return fig_tres


#ANTES ERA LA DOSSS
def duracion_promedio_genero(data):
    data = data.dropna(subset=["duracion_min"])
    data["duracion_min"] = pd.to_numeric(data["duracion_min"], errors="coerce")

    agrupado = data.groupby("genero", as_index=False)["duracion_min"].mean()

    fig_cuatro = px.bar(agrupado,
                 x="genero", y="duracion_min",
                 labels={"genero":"Genero", "duracion_min":"Duracion promedio(minutos)"},
                 text="duracion_min"
                 )
    fig_cuatro.update_layout(
        xaxis_title="Genero",
        yaxis_title="Duracion promedio(minutos)",
        template="plotly_dark"
    )
    fig_cuatro.update_traces(marker_color="#f5c518", textposition="outside")
    return fig_cuatro


def test():

    body = html.Div([
        html.H3("Dashboard de Peliculas", style={"color":"#FFFFFF", "text-aling":"center"}),

        #DROPDOWN
        dbc.Row([
            dbc.Col([
                html.H4("Seleccione el Año", style={"color":"#FFFFFF"}),
                dcc.Dropdown(
                    options=[
                        {"label":"2021", "value":2021},
                        {"label": "2022", "value": 2022},
                        {"label": "2023", "value": 2023},
                        {"label": "2024", "value": 2024},
                    ],
                    value=2024,
                    id="ddAñoGeneral",
                    style={"color":"#000000"}
                )
            ],width=12)
        ],style={"margin-bottom":"20px"}),

        #FILA UNOOOO
        dbc.Row([
            dbc.Col([
                html.H4("Distribución de Calificaciones",style={"color":"#FFFFFF"}),
                dcc.Graph(id="figDistCalificaciones")
            ],width=6),
            dbc.Col([
                html.H4("Distribución de Géneros", style={"color": "#FFFFFF"}),
                dcc.Graph(id="figDistGeneros")
            ], width=6)

        ], style={"margin-bottom":"20px"}),

        #FILA DOOOOS
        dbc.Row([
            dbc.Col([
                html.H4("Cantidad de Estrenos por Fecha", style={"color":"#FFFFFF"}),
                dcc.Graph(id="figEstrenosFecha")
            ],width=6),
            dbc.Col([
                html.H4("Duración Promedio por Género", style={"color": "#FFFFFF"}),
                dcc.Graph(id="figDuracionGenero")
            ], width=6)
        ], style={"margin-bottom":"20px"})
    ], style={"background-color":"#000000", "padding":"20px"})
    return body

@callback([
    Output("figDistCalificaciones", "figure"),
    Output("figDistGeneros", "figure"),
    Output("figEstrenosFecha", "figure"),
    Output("figDuracionGenero", "figure"),
],
    Input("ddAñoGeneral","value")
)
def update_grafica(value_año):
    filtrado = data[data["estreno"].dt.year == value_año]
    fig_calificaciones = distribucion_calificaciones(filtrado)
    fig_generos = distribucion_generos(filtrado)
    fig_estrenos = estrenos_fecha(filtrado)
    fig_duracion = duracion_promedio_genero(filtrado)


    return fig_calificaciones,fig_generos,fig_estrenos,fig_duracion
