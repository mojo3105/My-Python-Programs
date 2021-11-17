print("Enter the fibbonnaccii number do you want to know ")
n=int(input())
def fibbonnaccii(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else :
        return fibbonnaccii(n-1)+fibbonnaccii(n-2)
print("Your fibbonnaccii number is", fibbonnaccii(n))
