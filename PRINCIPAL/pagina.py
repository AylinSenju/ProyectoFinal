import dash
import dash_bootstrap_components as dbc

from click import style
# import dash_2 as d2
from dash import Input, Output, dcc, html, callback
# import dashboard as ds
import informacion as info

# PAGINA PRINCIPAL
@callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return info.welcome()
    # elif pathname == "/page-1": # DASHBOARD PELICULAS
        # return d2.dashboard(), ds.dashboard()
    elif pathname == "/page-2": # DASHBOARD SERIES
        return html.P("Pagina :3")
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


def menu_dashboard():
    sidebar = html.Div(
        [
            html.Img(src="assets/imagenes/cine.jpg", width=220, height=100, style={"borderRadius": "15px"}),
            html.Hr(),
            html.P("El portal al mundo del cine.", style={"className":"lead", "textAlign":"center", "color":"white"}),
            dbc.Nav(
                [
                    dbc.NavLink("Presentación", href="/", active="exact"),
                    dbc.NavLink("Dashboard Peliculas", href="/page-1", active="exact"),
                    dbc.NavLink("Dashboard Series", href="/page-2", active="exact"),
                    dbc.NavLink("GitHub", href="https://github.com/AylinSenju/ProyectoFinal", active="exact", target="_blank"), # REVISAR LINK
                ],
                vertical=True,
                pills=True,
            ),
        ],
        className="SIDEBAR_STYLE" # estilo a la parte izquierda
    )

    content = html.Div(id="page-content", className="CONTENT_STYLE")

    return html.Div([dcc.Location(id="url"), sidebar, content]) # juntar sidebar con el contenido



if __name__ == "__main__":
    app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL], suppress_callback_exceptions=True)  # COLORES
    app.layout = menu_dashboard()
    app.run(debug=True)