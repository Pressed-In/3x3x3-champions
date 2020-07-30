import plotly.graph_objects as go
import pandas as pd
import chart_studio.plotly as py


excel_file = 'RESULTS.xlsx'

df = pd.read_excel(excel_file, 2).query('Tournament_Wins != "-"')

### MODIFYING THE DATA FRAME FOR PERCENTS% ###

df['Win_Rate_A'] = df['Win_Rate'].map('{:.2%}'.format)

### END ###

fig = go.Figure(data=[go.Table(
	# columnorder = [1,2,3,4,5],
	# columnwidth = [22, 30, 25, 25, 15],
    header=dict(values=[['Name'], ['Country'], ['Tournament Wins'], ['Tournament Entries'], ['Win Rate']],
                fill_color='#93ACB5',
                align='left'),
    cells=dict(values=[df.name, df.countryId, df.Tournament_Wins, df.Tournament_Entries, df.Win_Rate_A],
               fill_color='#E5ECF6',
               align='left'))
])

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
	)

fig.show()

py.plot(fig, filename = 'basic-table', auto_open=True)