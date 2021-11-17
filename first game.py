#stone paper scissor game
import time
import random
print("Welcome to stone paper scissor game")
print("Loading Please Wait....... ")
time.sleep(3)
print("Instructions :- You are getting total 5 chances to play please enter the input correctly otherwise you can loose")
print("Your total score will be declared out of 5")
flag=0
print("Enter your choice \nfor stone enter 1\nfor paper enter 2\nfor scissor enter 3")
lst=["stone", "paper", "scissor"]
i=1
while(i<6):
    a=int(input())
    b=random.choice(lst)
    if a==1 and b=='stone':
        print("We choose", b)
        print("Match tied")
    elif a==1 and b=='paper':
        print("We choose", b)
        print("Sorry you lose ")
    elif a==1 and b=='scissor':
        print("We choose", b)
        print("You have win this round")
        flag=flag+1
    elif a == 2 and b == 'stone' :
        print("We choose", b)
        print("You have win this round")
        flag = flag + 1
    elif a == 2 and b == 'paper' :
        print("We choose", b)
        print("Match tied")
    elif a == 2 and b == 'scissor' :
        print("We choose", b)
        print("Sorry you lose ")
    elif a == 3 and b == 'stone':
        print("We choose", b)
        print("Sorry you lose ")
    elif a == 3 and b == 'paper':
        print("We choose", b)
        print("You have win this round")
        flag = flag + 1
    elif a == 3 and b == 'scissor':
        print("We choose", b)
        print("Match tied")
    else :
        print("Sorry wrong input and you have lost your one chance")
    i=i+1
    if i<6:
        print("Loading for next chance...")
        time.sleep(1)
        print("Enter again")
    else:
        break
if flag<3:
   print("Your total score is =",flag)
   print("Sorry Better luck next time.")
elif flag>2:
    print("Your total score is =", flag)
    print("Congratulations you have perform great .Thank you. Please visit next time.")