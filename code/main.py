from dash import html, dcc
import dash
import yfinance
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly as py

# data functions
def get_ticker(ticker: str) -> yfinance.Ticker:
    return yfinance.Ticker(ticker)

def get_earnings(ticker: yfinance.Ticker) -> pd.DataFrame:
    df = ticker.earnings
    df.index = pd.to_datetime(df.index, format='%Y')
    df['margin'] = df['Earnings'] / df['Revenue']
    return df

def get_balance(ticker: yfinance.Ticker) -> pd.DataFrame:
    BALANCE_FIELDS = ['Short Long Term Debt', 'Long Term Debt', 'Total Assets']
    df = ticker.get_balancesheet(freq='yearly').T[BALANCE_FIELDS]
    df['debt'] = df['Short Long Term Debt'] + df['Long Term Debt']
    df['assets'] = df['Total Assets']
    df.index = pd.to_datetime(df.index)
    return df[['debt', 'assets']]


def title_div():
    div = html.Div([
        html.H1(children="Dash-board", className="title")
    ])
    return div

aapl = get_ticker('AAPL')

def earnings_div():
    aapl_earnings = get_earnings(aapl)
    earnings_fig = px.bar(aapl_earnings, y=['Revenue', 'Earnings'], barmode='group')
    margin_fig = px.line(aapl_earnings, y='margin', range_y=[-0.1, 0.5], markers=True)
    div = html.Div([
        dcc.Graph(id='earnings', figure=earnings_fig),
        dcc.Graph(id='margins', figure=margin_fig)
    ])
    return div

def balance_div():
    aapl_balance = get_balance(aapl)
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=aapl_balance.index,
            y=aapl_balance.debt,
            name='Debt',
            marker_color='indianred'
        )
    )
    fig.add_trace(
        go.Bar(
            x=aapl_balance.index,
            y=aapl_balance.assets,
            name='Assets',
            marker_color='green'
        )
    )
    div = html.Div([
        dcc.Graph(id='balance', figure=fig)
    ])
    return div

app = dash.Dash()
app.layout = html.Div([
    title_div(),
    earnings_div(),
    balance_div()
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8080)
