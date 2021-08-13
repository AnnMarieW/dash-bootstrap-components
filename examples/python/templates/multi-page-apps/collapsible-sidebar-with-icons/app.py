"""
This app creates an animated sidebar using the dbc.Nav component and some local
CSS. Each menu item has an icon, when the sidebar is collapsed the labels
disappear and only the icons remain. Visit www.fontawesome.com to find
alternative icons to suit your needs!

dcc.Location is used to track the current location, a callback uses the current
location to render the appropriate page content. The active prop of each
NavLink is set automatically according to the current pathname. To use this
feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FA])

sidebar = html.Div(
    [
        html.Div(
            [
                # width: 3rem ensures the logo is the exact width of the
                # collapsed sidebar (accounting for padding)
                html.Img(src=PLOTLY_LOGO, style={"width": "3rem"}),
                html.H2("Sidebar"),
            ],
            class_name="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(class_name="fas fa-home mr-2"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(class_name="fas fa-calendar-alt mr-2"),
                        html.Span("Calendar"),
                    ],
                    href="/calendar",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(class_name="fas fa-envelope-open-text mr-2"),
                        html.Span("Messages"),
                    ],
                    href="/messages",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    class_name="sidebar",
)

content = html.Div(id="page-content", class_name="content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# set the content according to the current pathname
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the home page!")
    elif pathname == "/calendar":
        return html.P("This is your calendar... not much in the diary...")
    elif pathname == "/messages":
        return html.P("Here are all your messages")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", class_name="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
