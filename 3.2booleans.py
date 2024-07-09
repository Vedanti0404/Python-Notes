from re import I


a=bool(True)
print(a,type(a))

if a :
    print("hello")
else:
    print("hi")

    # ==================

if not a :
    print("hello")
else:
    print("hi")

    # ==================

if a is True:
    print("hello")
else:
    print("hi")
    
    # ===================

if a is not False:
    print("hello")
else:
    print("hi")

    #====================

# everything in boolean is true except :

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# you can run if block on bool function: 

def myfunc(a,b):
    return a*b

# myfunc(2,3)

print(myfunc(4,5))

if myfunc(4,0):
    print("hello")
else:
    print("hi")


