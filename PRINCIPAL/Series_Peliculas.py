import dash
import pandas as pd
from dash import dcc, html, Dash, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

datap = pd.read_csv("data/Df_Peliculas_Limpio")
datas = pd.read_csv("data/Df_Series_Limpio")

datap["tipo"] = "Película"
datas["tipo"] = "Serie"
datas["estreno"] = None

dataset=pd.concat([datap,datas],ignore_index=True)


def promedio_calificaciones(data,genero):
    filtrado=data[data["genero"] ==genero]
    agrupao=filtrado.groupby("tipo", as_index=False)["calificacion"].mean()


    fig_uno=px.bar(
        agrupao,
        x="tipo",
        y="calificacion",
        text="calificacion",
        labels={"tipo":"Tipo", "calificacion":"Promedio de Calificación"},
        template="plotly_dark"
    )
    fig_uno.update_traces(textposition="outside",marker_color='#f5c518')

    return fig_uno


def distribucion_calificaciones(data,genero):
    filtrado=data[data["genero"]==genero]

    fig_dos=px.histogram(
        filtrado,
        x="calificacion",
        color="tipo",
        barmode="overlay",
        labels={"calificacion":"Calificación",
                "tipo":"Tipo"},
        template="plotly_dark"
    )
    fig_dos.update_layout(bargap=0.2, yaxis_title="Cantidad de Titulos")

    return fig_dos


def popularidad_genero(data,genero):
    filtrado=data[data["genero"]==genero]
    agrupao=filtrado["tipo"].value_counts().reset_index()
    agrupao.columns=["tipo","cantidad"]

    fig_tres=px.pie(
        agrupao,
        names="tipo",
        values="cantidad",
        template="plotly_dark",
        color="tipo"
    )
    return fig_tres


def creadores_directores(data, genero):
    filtrado = data[data["genero"] == genero]


    if "director" in filtrado.columns:
        directores = filtrado.groupby(["director"], as_index=False).agg(
            cantidad=("calificacion", "count"),
            promedio=("calificacion", "mean")
        )
        directores["tipo_persona"] = "Director"
        directores.rename(columns={"director": "nombre"}, inplace=True)
    else:
        directores = pd.DataFrame(columns=["nombre", "cantidad", "promedio", "tipo_persona"])


    if "creador" in filtrado.columns:
        creadores = filtrado.groupby(["creador"], as_index=False).agg(
            cantidad=("calificacion", "count"),
            promedio=("calificacion", "mean")
        )
        creadores["tipo_persona"] = "Creador"
        creadores.rename(columns={"creador": "nombre"}, inplace=True)
    else:
        creadores = pd.DataFrame(columns=["nombre", "cantidad", "promedio", "tipo_persona"])

    personas = pd.concat([directores, creadores], ignore_index=True)

    top = personas.sort_values("cantidad", ascending=False).head(5)

    fig = px.bar(
        top,
        x="nombre",
        y="cantidad",
        color="tipo_persona",
        text="promedio",
        labels={
            "nombre": "Nombre",
            "cantidad": "Cantidad de Producciones",
            "promedio": "Promedio de Calificación",
            "tipo_persona": "Tipo"
        },
        template="plotly_dark",
    )

    fig.update_traces(texttemplate='%{text:.2f}', textposition="outside")
    fig.update_layout(xaxis_tickangle=-45)

    return fig


def dasboard():

    body=html.Div([
        html.H3("Dashboard de Peliculas y Series", style={"color":"#FFFFFF","text-align":"center"}),

        #SELECCION DEL GENEROOO
        dbc.Row([
            dbc.Col([
                html.H4("Seleccione un Género", style={"color":"#FFFFFF"}),
                dcc.Dropdown(
                    options=[{"label":genero, "value":genero} for genero in dataset["genero"].unique()],
                    value="Acción",
                    id="ddGenero",
                    style={"color":"#000000"}
                )
            ],width=12)
        ], style={"margin-bottom": "20px"}),

        #GRAFICO UNOOOO
        dbc.Row([
            dbc.Col([
                html.H4("Distribución de Calificaciones", style={"color": "#FFFFFF"}),
                dcc.Graph(id="figDistCalif"
                )
            ],width=6),
            dbc.Col([
                html.H4("Promedio de Calificaciones por Tipo", style={"color": "#FFFFFF"}),
                dcc.Graph(id="figPromCalif")
            ],width=6)
        ], style={"margin-bottom": "20px"}),

        dbc.Row([
            dbc.Col([
                html.H4("Popularidad del Género", style={"color":"#FFFFFF"}),
                dcc.Graph(id="figPupularidadGen")
            ],width=6),
            dbc.Col([
                html.H4("Creadores/Directores con más Producciones", style={"color": "#FFFFFF"}),
                dcc.Graph(id="figAnalisis")
            ],width=6)
        ], style={"margin-bottom":"20px"})
    ],style={"background-color": "#000000", "padding": "20px"})
    return body


@callback(
[Output("figPromCalif", "figure"),
        Output("figDistCalif","figure"),
        Output("figPupularidadGen","figure"),
        Output("figAnalisis","figure")],

    [Input("ddGenero","value")]
)

def update_grafica(genero):
    fig_promedio=promedio_calificaciones(dataset,genero)
    fig_distribucion=distribucion_calificaciones(dataset,genero)
    fig_populariad=popularidad_genero(dataset,genero)
    fig_analisis=creadores_directores(dataset,genero)

    return fig_promedio,fig_distribucion,fig_populariad,fig_analisis