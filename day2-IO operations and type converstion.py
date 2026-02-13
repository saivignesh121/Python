# Read input from user
num=input()
print(type(num))#checking the type of the number
print(num)

#implicit type conversion
num1=int(input())
val1=float(input())
print(type(num1),type(val1))#checking the type of number and value
result=num1+val1
print(result)

num=int(input())#Read string type number
print(type(num))#checking type of num
num=num+10
print(num)

#converting integer to float,string and boolean
num=12
print(float(num))
print(str(num))
print(bool(num))

#converting float to int bool and str
num2=12.25
print(int(num2))
print(str(num2))
print(bool(num2))

