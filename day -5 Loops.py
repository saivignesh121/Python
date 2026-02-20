lst=[11,12,13,14,15]
for ind in range(0,5,1):
    if lst[ind]%2==0:
        print(lst[ind]," is even")
    else:
        print(lst[ind]," is odd")
#print even numbers from 20 to 40 with step value 2
for num in range(20,41,2):
    if(num%2==0):
        print(num)
#print even numbers from 20 to 40 with step value1
for num in range(20,41):
    if (num%2==0):
        print(num)
#print numbers from 1 to 100
for num in range(1,101):
    print(num,end="")'''
'''#print sum of n natural numbers
num=int(input())
total=0
for num in range(1,num+1):
    total=total+num
print(total)

i=10
n=22
sum=0
while i<n:
    sum+=i
    i=i+1
print(sum)

