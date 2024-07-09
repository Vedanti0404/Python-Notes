# # immutable list are called as tuple:

# # syntax
# from re import A


# tp=(1,2,3)
# print(tp)

# print(tp.count(2))

# # no other functions are allowed

# # like
# li=[1,2,3]
# li[2]=100
# print(li)

# # but this i not the case in a tuple as tuples are immutable:

# # tp[2]=100 #error

# # declaring tuple with only 1 element:

# tps=(1,)
# print(tps)

# # miscellaneous:

# # swapping two numbers:
# # remember the property of python of initializing altogether:
# a,b,c="rohit",67.55,0

# print(a)
# print(b)
# print(c)

# # in similar way you can swap the number

# a,b=b,a

# print(a)
# print(b)

# ===========================================================================================

# tuples: oredered , allow duplicates: UNCHANGABALE

# thistuple = ("apple", "banana", "cherry","apple","banana")
# print(thistuple)

# can be accesssed using the index

# print(thistuple[2])

# ====================================================================================

# tuple length:

# print(len(thistuple))

# ====================================================================================

# create tuple with one item: 
# compulsorily add comma

# otherwise the python won't recognise it as the tuple .

# tp=(1,)
# print(type(tp))
# ================================================================================

# tuples can contain multiple data types mixed and uniform both

# tp=(1,"rohit",98.03,False)
# print(tp)

# ====================================================================================

# tuple constructor or explicit declaration: 


tp=tuple((1,"rohit",98.03,False,"pro",10020))
print(tp)

# ========================================================================================

# accessing tuples: slicing

# print(tp[3])
# print(tp[2:5])
# print(tp[-4])
# print(tp[-3-1])
# print(tp[3::])
# print(tp[-4::2])

# =================================================================================

# check if the key exist:

# if "rohit" in tp:
#     print(tp.index("pro"))

# ======================================================================================

# updating the tuples: 

# normally its not possible to update a tuple but , we can change it to list and perform desired operations.

# li=list(tp)
# li.append("patil")
# tp=tuple(li)
# print(tp)

# =========================================================================================

# change tuple items:

# li=list(tp)
# li.append("patil")
# li[0:3]=["a",56,True] #changing complete range of the tuple: 
# tp=tuple(li)
# print(tp) 

# ========================================================================================
# note: you cannot add or remove items from a tuple: but you can when it is converted to the list

# add items: append(),insert(),extend()

# remove items: pop(),pop(i),remove(k),del tp[i],del tp,clear()

# sort(),reverse()

# copy(),extend()


# =========================================================================================

# unpacking tuples: 
# tp=(2,3,4,4,5,6,5)

# print(tp)
# (one,two,*three)=tp
# print(one)
# print(two)
# print(three)

# ============================================================================================

# # looping through the tuple

# for x in tp :
#     print(x,end=" ")
# print("\n")


# # using len and range fumction: 

# for i in range(len(tp)):
#     print(tp[i],end=" ")
# print("\n")

# # while loop

# j=0
# while (j is not len(tp)):
#     print(tp[j],end=" ")
#     j+=1

# print("\n")

# =====================================================================================

# join tuples:

tp=(1,2,3,4)
tp2=(5,6,7,8)
tp3=tp+tp2
print(tp3)

# this is the ionly way to join tuples as append function works only on list

# multiply tuples:

tp = tp*3 #u can multiply only with numbers(int)
print(tp)

# =====================================================================================

# tuple methods:

# count()	Returns the number of times a specified value occurs in a tuple

print(tp.count(4))
# index()	Searches the tuple for a specified value and returns the position of where it was found

print(tp.index(2))















