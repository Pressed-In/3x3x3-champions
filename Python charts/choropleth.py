import plotly.express as px
import pandas as pd
import chart_studio.plotly as py


##### READ EXCEL FILE ####

excel_file = 'RESULTS.xlsx'

cube = pd.read_excel(excel_file, 1)


#### BUILD CHART ####

fig = px.choropleth(cube,   locations="Country", 
                            locationmode="country names", 
                            color="Winner_Count", 
                            # hover_name="Country", 
                            #hover_data=["Female_Competitors", "Male_Competitors", "Total_Competitors"], 
                            color_continuous_scale="aggrnyl")

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
    )

fig.show()

py.plot(fig, filename = 'basic-choropleth', auto_open=True)