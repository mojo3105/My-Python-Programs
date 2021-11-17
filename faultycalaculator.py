print("Enter the first number")
a=int(input())
print("Enter the second number")
b=int(input())
print("Enter the operation i.e addition, subtraction, multiplication and division")
op=input()
if a==54 and b==6 and op=='+' :
   print("Your answer is 50")
elif a==54 and b==6 and op=='-' :
     print("Your answer is 62")
elif a==54 and b==6 and op=='*' :
     print("Your answer is 150")
elif a==54 and b==6 and op=='/' :
     print("Your answer is 8")
elif a!=54 and b!=6 and op=='+':
     print("answer is=")
     print(a+b)
elif a!=54 and b!=6 and op=='-':
     print("answer is=")
     print(a-b)
elif a!=54 and b!=6 and op=='*':
     print("answer is=")
     print(a*b)
elif a!=54 and b!=6 and op=='/':
     print("answer is=")
     print(a/b)
else :
     print("Please enter the valid input")
