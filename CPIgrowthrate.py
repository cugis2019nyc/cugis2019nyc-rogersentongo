import pandas as pd
from plotly.offline import  plot
import plotly.graph_objs as go

#Importing the Data fron Excel into data frame
df = pd.read_excel('CPI.xlsx', sheet_name = 'cpi')
df

#read the x-axis data and the y-axis data into bar graph
trace = go.Bar(x= df['year'], 
               y=df['growthrate'],
               
               #add colors to the bars
               marker = dict(
                             color = df['growthrate'], 
                             colorscale = 'Jet'
                            )
              )
  
                 
layout = go.Layout(
                   #Title of the Graph
                   title = 'Consumer Price Index Growth Rate',
                   
                   #X-axis labe
                   xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text='Year'
                            
                        )
                    ),
                  
                   #Y-axis label 
                   yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text='Percentages'
                        )
                    )
                  )

#plot the data
fig = go.Figure(data=[trace], layout=layout)


plot(fig)


