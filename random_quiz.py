import random
#----random math quiz generator-----#
while(True):
    
    num=random.randint(1,7)
    arr=["+","-","*","/","%"];
    arr2=[]
    numbers=[]
    st=""
    ans="0.00"
    for i in range(0,num):
        arr2.append(arr[random.randint(0,4)]);
        #print(arr2[i])
    print("""answer the following question hint(use preority of the symbols)?\n\npress N or n fro next question..
          \nQ for quit""")
    
    
    for i in range(0,num):
        numbers.append(random.randint(0,999))
        print(numbers[i],arr2[i],end=" ")
        st=st+str(numbers[i])+arr2[i]
    
    numbers.append(random.randint(0,999))
    st=st+str(numbers[num])
    print(numbers[num])
    while(True):
        ans=input("Enter your ans (floting number till two decimal):")
        
        try:
            ans=float(ans)
        except:
            break
        eq=float("%.2f" % eval(st))
        if(ans==eq):
            print("correct ans...;-)")
            break;
        else:
            print("wrong ans...:-0")
    if(ans=="Q" or ans=="q"):
        break;
print("Byby...;-)")
        
        