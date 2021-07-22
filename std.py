import csv 
import math
with open('class2.csv',newline='') as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
marks=[]
marksTotal=0
for i in range(len(data)):
    marksTotal+=float(data[i][1])
    marks.append(float(data[i][1]))
n=len(marks)
meanmarks=marksTotal/n
print(meanmarks)
squariadlist=[]
sum=0
for i in range(len(data)):
    a=float(data[i][1])-meanmarks
    a=a**2
    sum+=a
    squariadlist.append(a)
result=sum/n
std=math.sqrt(result)
print(std)
import pandas as pd
import plotly.express as px
df=pd.read_csv('class2.csv')
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type='line',y0=meanmarks,y1=meanmarks,x0=0,x1=n)])
fig.show()