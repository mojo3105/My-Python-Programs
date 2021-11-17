age=0
print("Enter your age")
age=int(input())
while(age>130):
    print("Please enter valid age")
    age=int(input())
    if age < 100:
        break
if age<18:
    print("You are not eligible for driving")
elif age==18:
    print("Get your driving licence first ")
else :
    print("You are eligible for driving")
