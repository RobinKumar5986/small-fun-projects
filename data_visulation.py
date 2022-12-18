import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import random
def input_method_line():
    try:
        n=int(input("enter the number of cordinate:"))
        x=[]
        y=[]
        print("input X axis cordinates:")
        for i in range(0,n):
            x.append(float(input()))
        print("input Y axis cordinates:")
        for i in range(0,n):
            y.append(float(input()))
        np.array(x)
        np.array(y)
       
        pl.xlabel("x-axis")
        pl.ylabel("y-axis")
        
        pl.plot(x,y,'bo',linestyle="dashdot")
        pl.show()
    except:
        print("some error has occur")
        

#----exel visulation----#
def exel():
    fname=input("file address:")
    data=pd.read_csv(fname)
    column=data.columns[1:]
    column=list(column)
    x_axis=[]
    
    color=[]
    for i in range(len(data.columns)+2):
        color.append('#%06X' % random.randint(0, 0xFFFFFF))
        
        
    for i in range (0,len(data.index)):
       x_axis.append(i)
    for i in range(1,len(column)+1):
        X=list(data.iloc[:,i])
       
        #print(X,"\n------------------------------------------\n")
        pl.title(fname,color="red")
        pl.plot(x_axis,X,color=color[i],label=column[i-1])
        pl.legend(loc="upper left")
        
    #Y=list(data.iloc[:,x])
    #pl.plot(x_axis,Y,color[x+1])
    pl.show() 
    print(len(data.index))

#------pie chart--------#
def pie_chart():
    fname=input("file address:")
    data=pd.read_csv(fname)
    color=[]
    column=data.columns[1:]
    column=list(column)
    for i in range(len(data.columns)+2):
        color.append('#%06X' % random.randint(0, 0xFFFFFF))
        
    all_data=[]
    for i in range(1,len(column)+1):
        X=list(data.iloc[:,i])
        all_data.append(sum(X)/len(X))
    pl.title(fname,color="red")
    pl.pie(all_data,labels=column,colors=color,autopct="%1.1f%%")
    pl.show()
    
#-----bar graph-----#
def bar_graph():
    fname=input("file address:")
    data=pd.read_csv(fname)
    color=[]
    column=data.columns[1:]
    column=list(column)
    for i in range(len(data.columns)+2):
        color.append('#%06X' % random.randint(0, 0xFFFFFF))
        
    x_axis=[]
    for i in range (0,len(data.index)):
       x_axis.append(i)
    for i in range(1,len(column)+1):
        X=list(data.iloc[:,i])
        pl.bar(x_axis,X,color=color[i],label=column[i-1])
        pl.legend(loc="upper left")
    pl.show()
    
#---main function---#

print("------data visulation Menu-------")
print("1.normal line graph\n2.line graph\n3.pie chart\n4.bar graph\n5.exit\n")

while(True):
    ch=int(input("enter your choice : "))
    if(ch==1):
        input_method_line()
    elif(ch==2):
        exel()
    elif(ch==3):
        pie_chart()
    elif(ch==4):
        bar_graph()
    else:
        break
    
