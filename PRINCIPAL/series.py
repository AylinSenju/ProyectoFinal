import dash
import pandas as pd
from dash import dcc, html, Dash, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

data = pd.read_csv("DATA/Df_Series_Limpio")

def mejores(data):
    datas = data.sort_values(by="calificacion", ascending=False)
    data_top = datas.head(10)
    fig = px.bar(data_top, x="nombre", y="calificacion",
                 title="Ranking de Mejores Series",
                 labels={"nombre": "Series", "calificacion": "Calificación"})

    fig.update_layout(xaxis_title="Nombre de la Serie", yaxis_title="Calificación", template="seaborn")
    fig.update_traces(marker_color="#f9d659")
    return fig


def peores(data):
    datas = data.sort_values(by="calificacion", ascending=True)
    data_top = datas.head(10)
    fig = px.bar(data_top, x="nombre", y="calificacion",
                 title="Ranking de Peores Series",
                 labels={"nombre": "Series", "calificacion": "Calificación"})

    fig.update_layout(xaxis_title="Nombre de la Serie", yaxis_title="Calificación", template="seaborn")
    fig.update_traces(marker_color="#f9d659")
    return fig

def genero(data):
    genero_promedio = data.groupby("genero")["calificacion"].mean().reset_index()

    fig = px.pie(genero_promedio, values="calificacion", names="genero",
                 title="Ranking Promedio por Género")
    return fig



def top_5_por_genero(df, genero):
    filtro_genero = df[df['genero'] == genero]
    top_5 = filtro_genero.sort_values(by='calificacion', ascending=False).head(5)
    fig = px.bar(top_5, x="nombre", y="calificacion",
                 title=f"Top 5 Series en Género: {genero}",
                 labels={"nombre": "Series", "calificacion": "Calificación"})
    fig.update_layout(xaxis_title="Nombre de la Serie", yaxis_title="Calificación", template="seaborn")
    fig.update_traces(marker_color="#f9d659")
    return fig



def distribucion(data):
    fig = px.histogram(data, x="calificacion", nbins=20,
                       title="Distribución de Calificaciones",
                       labels={"calificacion": "Calificación"})
    fig.update_layout(xaxis_title="Calificación", yaxis_title="Cantidad de Series")
    fig.update_traces(marker_color="#f9d659")
    return fig




def dashboard():
    return html.Div([
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.H4("Selecciona una gráfica:", style={"color": "#f5c518"}),
                        html.Hr(),
                        dcc.Dropdown(
                            id="graph-dropdown",
                            options=[
                                {"label": "Mejores Series", "value": "mejores"},
                                {"label": "Peores Series", "value": "peores"},
                                {"label": "Promedio de Calificación por Género", "value": "genero"},
                                {"label": "Top 5 por Género", "value": "top_por_genero"},
                                {"label": "Distribución de Calificaciones", "value": "distribucion"}
                            ],
                            placeholder="Selecciona una opción",
                            style={"width": "50%", "padding": "3px"}
                        ),
                        html.Div(id="graph-container")
                    ], style={"backgroundColor": "#FFFFFF", "padding": "20px"})
                )
            ]
        ),
    ])


@callback(Output("graph-container", "children"), [Input("graph-dropdown", "value")])
def update_grafica(selected_graph):
    if selected_graph == "mejores":
        return dcc.Graph(figure=mejores(data))
    elif selected_graph == "peores":
        return dcc.Graph(figure=peores(data))
    elif selected_graph == "genero":
        return dcc.Graph(figure=genero(data))
    elif selected_graph == "top_por_genero":
        return html.Div([
            dcc.Dropdown(
                id="genre-dropdown",
                options=[{"label": genero, "value": genero} for genero in data["genero"].unique()],
                placeholder="Selecciona un género",
                style={"width": "50%", "margin-bottom": "20px"}
            ),
            html.Div(id="top-graph-container")
        ])
    elif selected_graph == "distribucion":
        return dcc.Graph(figure=distribucion(data))
    return html.Div()


@callback(Output("top-graph-container", "children"), [Input("genre-dropdown", "value")])
def update_top_genero(selected_genre):
    if selected_genre:
        return dcc.Graph(figure=top_5_por_genero(data, selected_genre))
    return html.Div("Selecciona un género para ver el Top 5")



if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = dashboard()
    app.run(debug=True)
