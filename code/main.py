import dash
from dash import html


def title_div():
    div = html.Div([
        html.H1(children="Dash-board", className="title")
    ])
    return div


app = dash.Dash()
app.layout = html.Div([
    title_div()
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8080)
