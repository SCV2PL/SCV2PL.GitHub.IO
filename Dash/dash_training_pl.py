# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import io
from base64 import b64encode

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

buffer = io.StringIO()

app = dash.Dash(__name__)

colors = {
    'background': '#313b4e',
    'text': ' #98c13d'
    
}

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT9R_mgljVOgzZIxM486fwlpk3WP10CA-rkZvfVIDNU2DqxL3gu7RRL7szZbZshWP8hcW2qKQPLJkBo/pub?gid=308673085&single=true&output=csv')

fig = px.scatter(df, x="% Zaszczepionych", y="Zgony / 10000 mieszkańców",
                 size="Populacja / 10000", color="Województwo", hover_name="Powiat", title="2021-12-30",
                 size_max=60, range_x=[25,75], range_y=[0,4.5],)
                 
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


fig.write_html(buffer)
                 
html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()
                 
app.layout = html.Div([
    dcc.Graph(
        id='',
        figure=fig),
    html.H1(children=''),

    html.Div(children='''
        14 Dniowa Suma Zgonów / 10000 Mieszkańców z Populacji Dla Danego Regionu - Na Poziomie Powiatów vs Poziom Zaszczepienia (%): Dla Szczytu z Dnia 2021-12-30.
    '''),
    html.A(
        html.Button("Download HTML"), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="dash_training_pl.html"
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
# https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c/edit#gid=308673085
