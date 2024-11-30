from dash import dcc, html, Dash, callback, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

# dcc -- dash core components
# html

def welcome():
    body = html.Div(
        [
            html.H3("SENSACINE"), # title
            html.Img(src="assets/imagenes/sensacine.png"),
            # html.P("Objetivo: Mostrar como funciona la libreria Dash", className="custom_p"), # parrafo
            html.Hr(), # linea horizontal
            # html.Img(src="ruta de la imagen", wight=200, height=200, title="aa")
            html.H4("INTEGRANTES"), # Puntos
            html.Ul(
                [
                    html.Li("ANGEL JAVIER GONZALEZ PRECIADO"),
                    html.Li("BIRON JADHIEL GONZALEZ RAMIREZ"),
                    html.Li("AYLIN YAEL MASCAREÑO ZENDEJAS"),
                    html.Li("SHERLYN RAMIREZ VELAZQUEZ"),
                    html.Li("GABRIEL ROMERO JERONIMO"),
                    html.Li("ANGELICA VANESA TAPIA CARRO"),
                    html.Li("")
                ]
            ) # Lista ordenada
        ]
    )
    return body


if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = welcome()
    # app.layout = dashboard()
    # app.run(debug=True)

