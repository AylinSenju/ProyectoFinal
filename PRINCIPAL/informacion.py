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
                    html.H4("Dashboards:", style={"color": "#f5c518"}),
                    html.P(
                         "DASHBOARD PELICULAS:"
                         " En esta seccion presentaremos 4 graficas donde se van a poder apreciar las distribucion de peliculas"
                         " por genero, calificacion y la duracion promedio por genero. En la parte superior vemos un caja donde se seleccionaran"
                         " los años para que nos de estadisticas de dichos años y como ultima grafica tenemos las fechas de estreno del año seleccionado",
                         style={"color": "black"},
                    ),

                     html.P(
                        "DASHBOARD SERIES:"
                        " En esta otra seccion se presentara garficas, las cuales ayudana poder visualizar"
                        " las mejores series dividias por  mejores/ peores, promedio de calificacion por genero, top 5 por genero y"
                        " la distribucion de calificaciones que hay de todas las series. ",
                        style={"color": "black"},),
                    html.P(
                      "DASBOARD PELICULAS Y SERIES: "
                      "Divido por genero, en este dashboard se presenta la informacion acerca de la distribucion de calificacion"
                      " de peliculas y series, asi como el promedio de estas, del genero seleccionado, asi como la popularidad del genero"
                      " en peliculas y serie y por utlimo los creadores/directores con mas producciones dentro del mismo genero."

                    ),
                ],
                style={"padding": "20px"},
            ),
        ]
    )
    return body

