num=int(input())
if ((num%2==0) and (num>=0)):
    print ("positive Even")
elif ((num%2==0) and (num<0)):
     print ("Negative Even")
elif ((num%2==1) and (num>0)):
    print("positive odd")
elif ((num%2==1) and (num<0)):
    print("negative odd")
else:
    print("enter a valid number")
    
num1,num2,num3= map(int,(input().split()))
if (num1>num2)and (num1>num3):
     print("num1 is greater")
elif (num2>num3):
     print("num2 is greater")
else :
     print("num3 is greater")
