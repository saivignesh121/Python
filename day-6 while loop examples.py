#while loop problems
#print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
#print even numbers between 10 to 40
i=10
while i<=40:
    if i%2==0:
        print( i,"even")
    i+=1
#print odd numbers between 1-50
i=1
while i<=50:
    if i%2==1:
        print(i,"odd")
    i+=1
#print which is even and which is odd
lst=[1,2,3,4,5,6,7,8,9]
ind=0
while ind <len(lst):
    if lst[ind]%2==0:
        print(lst[ind],"even")
    else:
        print(lst[ind],"odd")
    ind+=1
    
        
   

