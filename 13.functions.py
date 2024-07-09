def prints(a):

    '''

    this is called a docstring, which is comment inside a function.

    '''

    print(a*a)
    print("hello world")

w=int(input("enter any number: "))
prints(w)

# to find out the docstring 
help(prints) #this will print the docstring.

# second way

print(prints.__doc__)


# clean code example.

def is_even(n):
    return (n%2==0)

print(is_even(6))

# global and local same name:

a = 34

def func():
    a = 50
    return a

print(func())
print(a)

# here we can see that both 