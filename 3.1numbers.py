x=34
print(x,type(x))

x=45.6
print(x,type(x))

x=25-2j
print(x,type(x))

x=4.5e3
print(x,type(x))

# typecastingh between  numbers: 

# a=int(4+5j) #not possible 

a=complex(34.5)
print(a,type(a))



import random

print(random.randrange(1, 10))

# ===============================================

# isinstance operator: checks whether the variable is data type  or not

x=45.99
print(isinstance(x,float))