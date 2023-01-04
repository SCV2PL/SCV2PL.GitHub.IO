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
    'text': '#169dd5'
    
}

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT9R_mgljVOgzZIxM486fwlpk3WP10CA-rkZvfVIDNU2DqxL3gu7RRL7szZbZshWP8hcW2qKQPLJkBo/pub?gid=1516485369&single=true&output=csv')

fig = px.scatter(df, x="% Vaccinations", y="Deaths / 10000 inhabitants",
                 size="Population / 10000", color="Voivodeship", hover_name="District", title="2021-12-30",
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
        14 Days Total Deaths / 10,000 Inhabitants From The Population For a Given Region - At The Districts Level vs Vaccination Level (%): For The Vertex From The Day 2021-12-30. Point size = population size.
    '''),
    html.A(
        html.Button("Download HTML"), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="dash_training_en.html"
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
# https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c/edit#gid=1516485369
