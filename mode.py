import csv 
from collections import Counter
with open('SOCR.csv',newline='') as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
newData=[]
for i in range(len(data)):
    newData.append(float(data[i][1]))

modeData=Counter(newData)
modeRange={"50 to 60":0,"60 to 70":0,"70 to 80":0}
for Height,occurence in modeData.items():
    if 50<float(Height)<60:
        modeRange["50 to 60"]+=occurence
    elif 60<float(Height)<70:
        modeRange["60 to 70"]+=occurence
    elif 70<float(Height)<80:
        modeRange["70 to 80"]+=occurence
mrange,moccurence=0,0
for range,occurence in modeRange.items():
    if occurence>moccurence:
        mrange,moccurence=[int(range.split(" to ")[0]),int(range.split(" to ")[1])],occurence
mode=float((mrange[0]+mrange[1])/2)
print(mode)