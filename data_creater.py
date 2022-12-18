import numpy as np 
import random 
import pandas as pd
#random data generatir 
def generator():
    try:
        n=int(input("enter the number of fields : "))
        rang=int(input("enter the number of random generation : "))
        dict={}
        for i in range(0,n):
            name=input("Enter the filed name : ")
            dict[name]=np.random.rand(rang)
        data=pd.DataFrame(dict)
        name=input("enter the data file name : ")
        data.to_csv(name+".csv")
        print(name+".csv file created successfully...!!!")
    except:
        print("something went wromg")

generator()
while(True):   
    ans=input("Want to create more files [Y/N]? : ")
    if (ans=="N" or ans=="n"):
        break
    generator()
