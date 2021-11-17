l1=[]
sum=0
i=0
print("how many numbers do you want to enter")
nos= int(input())
for items in range(0 , nos):
    print("enter your number")
    items = int(input())
    l1.append(items)
    sum= sum + items
    items = items + 1
print("Your list is ready")
print(l1)
print("Sum of all elements in list is ")
print(sum)
print("The natural numbers upto 100 is ")
while(1):
    i = i + 1
    print(i)
    if i==100:
        break
