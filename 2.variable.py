
# # no need of data type like we needed in c , directly write the name of the avariable using the variable defining rules.
# #example:
# x=4
# print(x)
# # here x is the variable
# # 4 is the value assigned to the variable
# # here the python is smarter than the c lang to analyse that the value assigned to the integer is int type
# x=4.5
# print(x)
# # x is holding float
# x="hello world" 
# print(x)
# # x is now a string
# x='f' # = is a sssignment statement.
# # remember string is also a char in python no special char type in python
# print(x)

# # now we came to know that the python interprets the data type on its own:
# # so lets learn about the various datatypes:and how to knoe it using type function

var="""rohit"""
print(var,end=" ")
print(type(var))
var=4
# note that same variable can hold different data types without typecasting
print(var,type(var))
var=55.6
print(var,type(var))
var=True
print(var,type(var))
var={1,2.44,"hi",1 ,"set only stores unique value"}
print(var,type(var))
var=(2,"6",4.55)
print(var,type(var))
var={"hi":"greeting","bye":"good bye"}
print(var,type(var))
var={45,46,"tor",45}
print(var,type(var))

# ===================================================================================


# operations on the variable: 

# 1) conacatenation of strings:
# str1="rohit "
# str2="patil"
# print(str1,str2) # + or ,

# num=4
# print(num + str1)#error as number cannot be added to string

# but we can multiply to print the same line multiple times
# print(num*str1)#but this will print it on the same line

# print(num*"rohit\n")#so use \n in the string itself


# # ==================================================================================

# 2)number printing in statements: 

n=45
print("hello your age is",n)
print("you can manipulate it",n+45)

# printing number as a string :
print("you can print number as a string but if you print it as string it cannot be manupulated")


# # ====================================================================================

# # typecasting : note you cannot typecast a string  to integer
# n=str(n)
# print("now when n is string you can even concatenate it "+ n)
# print("or you can concatente using \",\" operator",n)
# # print("yes but now you cannot manupualate it "+ n-4) #  not allowed.

# n=float(n)

# print(n)

# boolean_val=True

# print(int(boolean_val)) 

# boolean_val=False

# print(int(boolean_val)) 

# print(str(boolean_val))

# print(float(boolean_val))

# r=0

# print(r,type(r))

# print(bool(r),type(r))


# ======================================================================================
#   assingning same value to multiple variables: 

# x=y=z="oranges"

# print(x)
# print(y)
# print(z)


# global variables: 

x="hello" #<----------preference only when the their is no local 
def func():
    x="hi"  #--------------------->local variable: given preference.
    print(x,"world")

func() #<--------------------------- calling a function.

print(x,"world")






