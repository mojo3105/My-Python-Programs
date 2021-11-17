print("welcome to our H n M system")
members = {1: "rahul", 2: "ruhan", 3: "monisha"}

print(members)
n = int(input())
if n == 1:
    print("welcome rahul")
    print("1-edit,2-see details")
    h = int(input())
    if h == 1:
        rahul()
    elif h == 2:
        details(rahul)


elif n == 2:
    print("welcome ruhan")
    print("1-edit,2-see details")
    h = int(input())
    if h == 1:
        ruhan()
    elif h == 2:
        details(ruhan)

elif n == 3:
    print("welcome monisha")
    print("1-edit,2-see details")
    h = int(input())
    if h == 1:
        monisha()
    elif h == 2:
        details(monisha)

else:
    print("u r not a existing member")