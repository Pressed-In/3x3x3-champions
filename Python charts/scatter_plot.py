################    THE SETUP   #######################

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import chart_studio.plotly as py

excel_file = 'RESULTS.xlsx'

cube = pd.read_excel(excel_file).query('Date != "1982-6-5"')

#####################   THE DATA STUFF  ########################

fig = px.scatter(cube, x="Date", y="Best Time (seconds)", color="Format", 
	hover_name="personName", hover_data=["Competition_Name"],
	opacity=0.65,
	)

fig.update_layout(
    legend=go.layout.Legend(
        x=0.88,
        y=0.973,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),

        #bgcolor="LightSteelBlue",
        bgcolor="#A9D3FF",

        bordercolor="Black",
        borderwidth=2
    )
)

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
    )

fig.show()

py.plot(fig, filename = 'basic-scatter', auto_open=True)