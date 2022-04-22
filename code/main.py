import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import yfinance
from dash import html, dcc, Output, State, Input


# data functions
def get_ticker(ticker: str) -> yfinance.Ticker:
    return yfinance.Ticker(ticker)


def get_earnings(ticker: yfinance.Ticker) -> pd.DataFrame:
    df = ticker.earnings
    df.index = pd.to_datetime(df.index, format='%Y')
    df['margin'] = df['Earnings'] / df['Revenue']
    return df


def get_balance(ticker: yfinance.Ticker) -> pd.DataFrame:
    BALANCE_FIELDS = ['Total Liab', 'Total Assets']
    df = ticker.get_balancesheet(freq='yearly').T[BALANCE_FIELDS]
    df['debt'] = df['Total Liab']
    df['assets'] = df['Total Assets']
    df.index = pd.to_datetime(df.index)
    return df[['debt', 'assets']]


def title_div():
    div = html.Div([
        html.H1(children="Dash-board", className="title")
    ])
    return div


def ticker_button():
    div = html.Div([
        dcc.Input(
            id='input-ticker',
            type='text',
            value='AAPL'
        ),
        html.Button('Submit', id='input-on-submit', n_clicks=0)
    ])
    return div


def earnings_div():
    div = html.Div([
        dcc.Graph(id='earnings'),
        dcc.Graph(id='margins')
    ])
    return div


def balance_div():
    div = html.Div([
        dcc.Graph(id='balance')
    ])
    return div


app = dash.Dash()
app.layout = html.Div([
    title_div(),
    ticker_button(),
    earnings_div(),
    balance_div()
])


@app.callback(
    Output('earnings', 'figure'),
    State('input-ticker', 'value'),
    Input('input-on-submit', 'n_clicks')
)
def ticker_earnings_renderer(input_ticker, n_clicks):
    ticker = get_ticker(input_ticker)
    earnings_df = get_earnings(ticker)
    earnings_fig = px.bar(earnings_df, y=['Revenue', 'Earnings'], barmode='group')
    return earnings_fig


@app.callback(
    Output('margins', 'figure'),
    State('input-ticker', 'value'),
    Input('input-on-submit', 'n_clicks')
)
def ticker_margins_renderer(input_ticker, n_clicks):
    ticker = get_ticker(input_ticker)
    earnings_df = get_earnings(ticker)
    margins_fig = px.line(earnings_df, y='margin', range_y=[-0.1, 0.5], markers=True)
    return margins_fig


@app.callback(
    Output('balance', 'figure'),
    State('input-ticker', 'value'),
    Input('input-on-submit', 'n_clicks')
)
def ticker_margins_renderer(input_ticker, n_clicks):
    ticker = get_ticker(input_ticker)
    balance_df = get_balance(ticker)
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=balance_df.index,
            y=balance_df.debt,
            name='Debt',
            marker_color='indianred'
        )
    )
    fig.add_trace(
        go.Bar(
            x=balance_df.index,
            y=balance_df.assets,
            name='Assets',
            marker_color='green'
        )
    )
    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8080)
