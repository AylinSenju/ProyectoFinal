from dash import dcc, html, Dash
import dash_bootstrap_components as dbc


def welcome():
    body = html.Div(
        [
            html.Div(
                [
                    html.Img(src="assets/imagenes/sensa.jpg", width=220, height=100),
                    html.P("El sitio perfecto para los amantes del cine."),
                ], style={"textAlign": "center", "color": "black", "padding": "20px"},
            ),
            html.Hr(),
            html.Div(
                [
                    html.H4("Integrantes del proyecto:", style={"color": "#f5c518"}),
                    html.Ul(
                        [
                            html.Li("Angel Javier Gonzalez Preciado"),
                            html.Li("Biron Jadhiel Gonzalez Ramírez"),
                            html.Li("Aylin Yael Mascareño Zendejas"),
                            html.Li("Sherlyn Ramirez Velazquez"),
                            html.Li("Gabriel Romero Jeronimo"),
                            html.Li("Angelica Vanesa Tapia Carro"),
                        ],
                        style={"color": "black"},
                    ),
                ],
                style={"padding": "20px"},
            ),
            html.Hr(),
            html.Div(
                [
                    html.H4("Acerca del proyecto:", style={"color": "#f5c518"}),
                    html.P(
                        "Este proyecto tiene como objetivo principal ofrecer un análisis profundo del mundo del cine "
                        "y la televisión mediante el uso de herramientas de visualización aprendidas en 'Programación para la "
                        "Super Extracción de Datos'.",
                        style={"color": "black"},
                    ),
                    html.P(
                        "Incluye un sistema de dashboards interactivos que permite explorar información detallada sobre películas y series, "
                        "como calificaciones, géneros más populares, las más taquilleras, etc.",
                        style={"color": "black"},
                    ),
                ],
                style={"padding": "20px"},
            ),
        ]
    )
    return body


if __name__ == "__main__":
    app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])  # Tema Bootstrap oscuro
    app.layout = welcome()
    app.run_server(debug=True)
