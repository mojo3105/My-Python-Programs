print("Enter the number of which factorial do you want to find")
n=int(input())


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)

print("Fatorial by recursive method is ",factorial_recursive(n))
