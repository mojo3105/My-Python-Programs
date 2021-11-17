"""
x = object()
y = object()
x_list = [x]*10
y_list = [y]*10
big_list = x_list+y_list
print(" x_list contains %d objects " % len(x_list))
print(" y_list contains %d objects " % len(y_list))
print(" big_list contains %d objects " % len(big_list))
if x_list.count(x) == 10 and y_list.count(y) == 10:
  print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
  print("Great!")
  """


def timing():
  import datetime

  return (datetime.datetime.now())


time = timing()
date_time = time.strftime("%d:%m:%y , %H:%M ")


def rahul():
  print(" what do u want to edit- diet / excercise ")
  print(" enter 1 for diet \n enter 2 for excercise ")

  x = int(input("enter number "))
  if x == 1:

    v = int(input("input no of meals "))
    for i in range(1, v + 1):
      with open("rahuldiet.txt", "a+") as fp:
        fp.write(date_time)
        fp.write(input())
        fp.write("\n")
        print("ur meal is saved now")

  elif x == 2:
    v = int(input("number of excercise "))
    for i in range(1, v + 1):
      with open("rahulexc.txt", "a+") as fp:
        fp.write(date_time)
        fp.write(input())
        fp.write("\n")
        print("ur excercise is saved now")
  return ()


def ruhan():
  print(" what do u want to edit- diet / excercise ")
  print(" enter 1 for diet \n enter 2 for excercise ")

  x = int(input("enter number "))
  if x == 1:

    v = int(input("input no of meals "))
    for i in range(1, v + 1):
      with open("ruhandiet.txt", "a+") as sp:
        sp.write(date_time)
        sp.write(input())
        sp.write("\n")
        print("ur meal is saved now")

  elif x == 2:
    v = int(input("number of excercise "))
    for i in range(1, v + 1):
      with open("ruhanexc.txt", "a+") as sp:
        sp.write(date_time)
        sp.write(input())
        sp.write("\n")
        print("ur excercise is saved now")
  return ()


def monisha():
  print(" what do u want to edit- diet / excercise ")
  print(" enter 1 for diet \n enter 2 for excercise ")

  x = int(input("enter number "))
  if x == 1:

    v = int(input("input no of meals "))
    for i in range(1, v + 1):
      with open("monishadiet.txt", "a+") as tp:
        tp.write(date_time)
        tp.write(input())
        tp.write("\n")
        print("ur meal is saved now")

  elif x == 2:
    v = int(input("number of excercise "))
    for i in range(1, v + 1):
      with open("monishaexc.txt", "a+") as tp:
        tp.write(date_time)
        tp.write(input())
        tp.write("\n")
        print("ur excercise is saved now")
  return ()


def details(name):
  if name == rahul:
    with open("rahuldiet.txt") as f:
      print(f.read())
      print("\n")
    with open("rahulexc.txt") as f:
      print(f.read())
  elif name == ruhan:
    with open("ruhandiet.txt") as f:
      print(f.read())
      print("\n")
    with open("ruhanexc.txt") as f:
      print(f.read())
  elif name == monisha:
    with open("monishadiet.txt") as f:
      print(f.read())
      print("\n")
    with open("monishaexc.txt") as f:
      print(f.read())
  return ()