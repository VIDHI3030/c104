import plotly.express as px
import csv 
with open ("coffee.csv") as sfile:
    df=csv.DictReader(sfile)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()