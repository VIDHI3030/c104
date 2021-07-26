import plotly.express as px
import csv 
with open ("percentage.csv") as sfile:
    df=csv.DictReader(sfile)
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()