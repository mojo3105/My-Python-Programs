n=18
i=0
flag=0
print("Enter the number less than 100")
a=int(input())
while(i<5):
     if a>18:
         print("Reduce your number")
         a=int(input())
         if a==18:
             print("Congratulations you have won the game ")
             flag=1
             break
         else :
             i = i + 1
             print("Try again you have",5-i, " chances left")
     elif a<18:
         print("Increase your number")
         a = int(input())
         if a == 18:
             print("Congratulations you have won the game ")
             flag =1
             break
         else:
             i = i + 1
             print("Try again you have",5-i, " chances left")
     elif a==18:
          print("Congratulations you have won the game in first attempt")
          flag=1
          break
if flag ==0:
   print("Sorry you lost the game better luck next time")