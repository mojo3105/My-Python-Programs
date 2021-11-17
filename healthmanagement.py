def timing():
  import datetime

  return (datetime.datetime.now())


time = timing()
date_time = time.strftime("%d:%m:%y , %H:%M ")

print("Welcome to MOJO Health Management Systems Pvt. Ltd.")
print("Hello Client Enter your Name")
name = input()

if name=='mohit':
    print("Welcome boss \n")
    print("What do you want to know about diet or exercise")
    inp=input()
    if inp =='diet':
        print("Enter 1 for see the details or 2 update ")
        no =int(input())
        if no==2:
            v = int(input("Input no of meals \n"))
            for i in range(1, v + 1):
                with open("mohitdiet.txt", "a+") as fp:
                    fp.write(date_time)
                    fp.write(input())
                    fp.write("\n")
            print("Your meal is saved now")
        elif no==1:
            f=open("mohitdiet.txt")
            content=f.read()
            print(content)
    elif inp=='exercise':
        print("Enter 1 for see the details or 2 update ")
        no = int(input())
        if no == 2:
            v = int(input("Input no of exercises \n"))
            for i in range(1, v + 1):
                with open("mohitexe.txt", "a+") as fp:
                    fp.write(date_time)
                    fp.write(input())
                    fp.write("\n")
            print("Your exercise is saved now")
        elif no == 1:
            f = open("mohitexe.txt")
            content = f.read()
            print(content)
elif name=='jay':
    print("What do you want to know about diet or exercise")
    inp = input()
    if inp == 'diet':
        print("Enter 1 for see the details or 2 update ")
        no = int(input())
        if no == 2:
            v = int(input("Input no of meals\n "))
            for i in range(1, v + 1):
                with open("jaydiet.txt", "a+") as fp:
                    fp.write(date_time)
                    fp.write(input())
                    fp.write("\n")
            print("Your meal is saved now")
        elif no == 1:
            f = open("jaydiet.txt")
            content = f.read()
            print(content)
    elif inp == 'exercise':
        print("Enter 1 for see the details or 2 update ")
        no = int(input())
        if no == 2:
            v = int(input("Input no of exercises\n "))
            for i in range(1, v + 1):
                with open("jayexe.txt", "a+") as fp:
                    fp.write(date_time)
                    fp.write(input())
                    fp.write("\n")
            print("Your exercise is saved now")
        elif no == 1:
            f = open("jayexe.txt")
            content = f.read()
            print(content)
elif name=='om':
    print("What do you want to know about diet or exercise")
    inp = input()
    if inp == 'diet':
        print("Enter 1 for see the details or 2 update ")
        no = int(input())
        if no == 2:
            v = int(input("Input no of meals\n "))
            for i in range(1, v + 1):
                with open("omdiet.txt", "a+") as fp:
                    fp.write(date_time)
                    fp.write(input())
                    fp.write("\n")
            print("Your meal is saved now")
        elif no == 1:
            f = open("omdiet.txt")
            content = f.read()
            print(content)
    elif inp == 'exercise':
        print("Enter 1 for see the details or 2 update ")
        no = int(input())
        if no == 2:
            v = int(input("Input no of exercises \n"))
            for i in range(1, v + 1):
                with open("omxe.txt", "a+") as fp:
                    fp.write(date_time)
                    fp.write(input())
                    fp.write("\n")
            print("Your exercise is saved now")
        elif no == 1:
            f = open("omexe.txt")
            content = f.read()
            print(content)
else :
    print("You are not a member of our exclusive system . So please kindly get your membership first then enjoy our services ")
