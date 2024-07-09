# input must be stored in a variable , you need not worry about the data type just give a variable and take the input, because data type is something managed by the python itself:

# from sys import flags
# from tokenize import Double


x=input("what is your name: ")
# note that input takes the string not character , onfact their is no concept of characters in python, everything  can be asked as an input including white space characters.

print("hello "+ x)#concatenation using + or ,
# note : by default the input is taken for string only:

# to take specific input mention the data type for the input function

y=float(input("enter your weight "))
print("your weight is "+ str(y))#converted the float to str before concatenation in the string but the number no more a number , so use

print("your weight is: ",y)
# arithmetic operations on y will prove that the y printed is number not a string

# long method
print("enter an number: ")
# num=input()#defalut input is always string.

num=int(input())
# note : int input will accept int only but while printiny you can type cast it

print("your answer is : "+str(num))

