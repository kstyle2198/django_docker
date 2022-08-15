from re import S
from django.shortcuts import render
# import plotly.graph_objects as go
import pandas as pd
from urllib.request import urlopen
import dash
import plotly.express as px
from dash import dash_table
from dash import html
from dash import dcc
from dash.dependencies import Output, Input, State
import dash_extensions as de  # pip install dash-extensions

# Create your views here.

# def covid(request):
#     src = urlopen('https://covid19.who.int/WHO-COVID-19-global-data.csv').readlines()
#     deco_source = [x.decode('utf-8').rstrip('\n').split(',') for x in src[1:]]
#     columns = ["date", "country_code", 'country', 'region', 'new_case', 'accum_case', 'new_death', 'accum_death', "None"]
#     df = pd.DataFrame(deco_source, columns = columns)
#     df = df.drop(columns='None')
#     countries = df.country.unique()
#     # print(countries)
#     df = df[df["country"] == "Republic of Korea"][:]
   
#     x = df.date[-300:].to_list()
#     y = df.new_case[-300:].astype('int64').to_list()

#     fig = px.line(x=x, y=y, title="Covid", labels={'x':'Date', 'y':'New Case'})
    
#     fig.update_layout(
#         title = {
#             'font_size': 24,
#             'xanchor': 'center',
#             'x': 0.5
#         }
#     )
#     chart = fig.to_html()
#     context = {'chart': chart}
#     return render(request, "covid.html", context)


from plotly.offline import plot
import plotly.graph_objects as go

def covid(request):
    x_data = [1,2,3,4, 5, 6, 7, 8]
    y1_data = [x**2 for x in x_data]
    y2_data = [x**3 for x in x_data]
    y3_data = [x**4 for x in x_data]
    
    fig = go.Figure()
    
    scatter1 = go.Scatter(x=x_data, y=y1_data,
                        mode='lines+markers', name='test1',
                        opacity=0.8, marker_color='green')
    scatter2 = go.Scatter(x=x_data, y=y2_data,
                        mode='lines+markers', name='test2',
                        opacity=0.8, marker_color='red', line=dict(color='royalblue', width=4, dash='dot'))
    scatter3 = go.Scatter(x=x_data, y=y3_data,
                        mode='lines+markers', name='test3',
                        opacity=0.8, marker_color='blue', line=dict(color='blue', width=4, dash='dash'))
    
    fig.add_trace(scatter1)
    fig.add_trace(scatter2)
    fig.add_trace(scatter3)
    
    fig.update_layout(title = 'Testing', xaxis_title='x', yaxis_title='y')
    
    plot_div = plot(fig,
               output_type='div')
    context = {'chart': plot_div}
    return render(request, "covid.html", context)

    