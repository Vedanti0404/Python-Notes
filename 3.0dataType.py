# int data type
# a=15
# b=-234
# c=0
# print("the numbers are",a,b,c)
# _________________________________
# # float data type
# d=12.55
# e=-123.333
# f=0.23
# print("the number are: ",d,e,f)
# ______________________________
# # complex data type
# p=1+34j
# q=23-3j
# r=-23-33j
# print("the numbers are : ",p,q,r)
# _________________________________
# # boolean
# print(a==b)
# print(bool(f))
# print(c==0)
# ____________________________
# strings
# x="ROHIT patil 234234"
# y='rohit patil'
# z='''rohit 
# patil is 
# good boy '''
# print(x)
# print(y)
# print(z)
# ____________________slicing_____________
# print(x[1])
# print(y[-4])#indexing
# print(x[-8:-4])
# print(x[2:6])
# print(y[4:])
# print(z[1:8])
# # _________printing length of the string_____
# print(len(x))
# # __________concatenation of the strings__________
# print(x+" hello "+y)
# p=x.capitalize()#capitalize the first letter
# print(p)
# _______________________________________
# a=x.lower()#lower case of complete string
# print(a)
# _____________________________
# y=x.count("2")#counts how many times a charcte has appered in that string
# print(y)
# ____________________________________
# l=x.isalpha()#gives true if char is alphabet
# o=x.isnumeric()#gives true if every char is numeric
# print(l)
# print(o)
#____________________________________
# and many more 
# ____________________________________
# list [] is a collection of mixed data types
# lists=[12,"rohit patil",["rohit patil",12,-2344.55],True]
# print(lists)
# print(lists[2][0][3:7])#indexing and slicing in list
# ___________________________
# appending any item in list
# q=lists.append(78)
# print(lists)
# ______________________________________
#deleting anything from the list
# d=lists.pop(2)
# print(lists)
# _______________________________
# removing any value without ststing the index
# b=lists.remove("rohit patil")
# print(lists)
# ____________________________________________
# 
# # tuple immutable
# tuples=(12,"34rohit patil",-314)
# print(tuples)
# print(tuples[0])#indexing
# print(tuples[1][2:])#slicing
# __________________________________
# #sets
# set1={233,34,222.34,341324,34}
# print(set1)
# ________________________________
# dictionary
# dict1={
#     "x": "rohit patil",
#     "y": "sujata patil"

# }
# print(dict1)#printing complete dictionary
# ________________________________________
# updating the dictionary
# dict1["x"]="jeetendra"
# print(dict1)
# _________________________________________
# deleting value from dictionary
# dict1.pop("x")
# print(dict1)
# ____________________________________
# accessing any element using key
# print(dict1["x"])
# _______________________________________
# typecasting
# aa=23.34
# ab=23dddd 
# print(aa+ab)#implicit
# print(int(aa))
# print(float(ab))#explicit

# print(b"hello")  bytes

# bytearray(5) byte array

# x=None none



# numbers:

# random numbers:
# 
# import random


# print(random.randrange(1,10))


# =============================================================================================

# explicit declaration of the data types :

x=34
print(x,type(x))
x=int(45)
print(x,type(x))

x=34.5
print(x,type(x))
x=float(0.9)
print(x,type(x))

x="rohit"
print(x,type(x))
x=str("youtube")
print(x,type(x))

x=34+9j
print(x,type(x))
x=complex(2+9j)
print(x,type(x))

x=False
print(x,type(x))
x=bool(True)
print(x,type(x))

x=["rohit ",34,45.6,True]
print(x,type(x))
x=list(("rohit ",34,45.6,True))
print(x,type(x))

x=set(("rohit ",34,24.55))
print(x,type(x))
x={"rohit ",34,24.55}
print(x,type(x))


x=tuple(("excuse me", 99, False))
print(x,type(x))

x=range(5)
print(x,type(x))

X=dict(age=34,rohit=38)
print(x,type(x))
x={"rohit ":38,"age":99}
print(x,type(x))

x=bytes(5)
print(x,type(x))

x=bytearray(5)
print(x,type(x))

x=memoryview(bytes(5))
print(x,type(x))









