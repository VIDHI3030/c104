import csv 
with open('SOCR.csv',newline='') as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
Height=[]
Weight=[]
heightTotal=0
weightTotal=0
for i in range(len(data)):
    heightTotal+=float(data[i][1])
    Height.append(float(data[i][1]))
    weightTotal+=float(data[i][2])
    Weight.append(float(data[i][2]))
n=len(Height)
meanHeight=heightTotal/n
meanWeight=weightTotal/n
print(meanHeight)
print(meanWeight)
