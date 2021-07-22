import csv 
import math

data=[60,61,65,63,98,99,90,95,91,96]
marks=[]
marksTotal=0
for i in data:
    marksTotal+=i
n=len(data)
meanmarks=marksTotal/n
print(meanmarks)
squariadlist=[]
sum=0
for i in data:
    a=i-meanmarks
    a=a**2
    sum+=a
    squariadlist.append(a)
result=sum/n