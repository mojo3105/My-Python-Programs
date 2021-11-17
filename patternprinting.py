i=1
a=0
print("Enter the number")
n=int(input())
print("Enter the boolean value 0 for false or 1 for ture")
b=int(input())
if b==1:
    while(i<=n):
        print(i*"*")
        i=i+1
else :
    i=n
    while(1):
        print(i*"*")
        i=i-1
        if i==0:
            break