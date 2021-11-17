# this program is about args and kwargs while using args and kwargs as an arguments use normal first then args and then kwargs
def funargs(normal, *args, **kwarg):
    #this is doc string args are tuple class
    print(normal)
    print(type(args))
    for items in args :
        print(items)
    print("Now I would like to introduce some of our heroes ")
    for key, value in kwarg.items():
        print(f"{key} is a {value} ")
mojo=["mohit", "arvind", "joshi"]
normal="This is normal"
kw={"Developer":"Mohit", "Deployer":"Pankaj", "Tester":"Shailesh"}
funargs(normal, *mojo, **kw)