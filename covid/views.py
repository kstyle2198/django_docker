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

def covid(request):
    src = urlopen('https://covid19.who.int/WHO-COVID-19-global-data.csv').readlines()
    deco_source = [x.decode('utf-8').rstrip('\n').split(',') for x in src[1:]]
    columns = ["date", "country_code", 'country', 'region', 'new_case', 'accum_case', 'new_death', 'accum_death', "None"]
    df = pd.DataFrame(deco_source, columns = columns)
    df = df.drop(columns='None')
    countries = df.country.unique()
    # print(countries)
    df = df[df["country"] == "Republic of Korea"][:]
   
    x = df.date[-300:].to_list()
    y = df.new_case[-300:].astype('int64').to_list()

    fig = px.line(x=x, y=y, title="Covid", labels={'x':'Date', 'y':'New Case'})
    
    fig.update_layout(
        title = {
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
        }
    )
    chart = fig.to_html()
    context = {'chart': chart}
    return render(request, "covid.html", context)

# if __name__ == "__main__":
#     covid()










# from django.shortcuts import render
# import plotly.express as px

# from core.forms import DateForm
# from core.models import CO2

# # Create your views here.
# def chart(request):
#     start = request.GET.get('start')
#     end = request.GET.get('end')

#     co2 = CO2.objects.all()
#     if start:
#         co2 = co2.filter(date__gte=start)
#     if end:
#         co2 = co2.filter(date__lte=end)

#     fig = px.line(
#         x=[c.date for c in co2],
#         y=[c.average for c in co2],
#         title="CO2 PPM",
#         labels={'x': 'Date', 'y': 'CO2 PPM'}
#     )

#     fig.update_layout(
#         title={
#             'font_size': 24,
#             'xanchor': 'center',
#             'x': 0.5
#     })
#     chart = fig.to_html()
#     context = {'chart': chart, 'form': DateForm()}
#     return render(request, 'core/chart.html', context)