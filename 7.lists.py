 #list

# li=["rohit ","vedant",67,67.88,"rohit"]

# print(li)#printing the list: 

# # accessing the SINGLE element 
# print(li[0])

# print(li[5])

# print(li[4])

# print(li[2])

# operations on list


# note: single list containing multiple datat types cannot be compared with each other hence they cannot be sorted
# so to make a sortable list always use a single datatyped list like array
# also it is although allowed to make a list with different data types but many functiions then cant be applied on it, but yes can be created.
# making sortable list below:
# li=[9,5,2,7,4,16]

# li.sort()
# print(li)
 
# li.reverse()
# print(li) 

# 3)slicing in the list

# li=[1,"r",3.14159,True,["patil",34]]#unsortable list

# print(li)

# print(li[2:])

# print(li[:])

# print(li[::-1])

# print(li[4:])

# print(li[4][0][0:3])

# li.reverse()#can be done on list with different data types

# note that sort() or reverse() changes the list permanantly but slicing don't

# print(li)

# print(li[2:5:2])

# # print(li[2:5:-2]) #note not to use negative slicing to skip the characters only -1 is allowed else the output will be blank list

# print(len(li))

# print(max(li))#similar to sort max and min won't work on the list having different data types: 

# some more operations on list

# li.append("wow") #insert at last

# print(li)

# li.insert(4,False) # insert at a specific position

# print(li)

# li.remove("r") #remove any particular element

# print(li)

# li.pop() #removes only the last element

# print(li)

# # print(li.index(True))

# print(li.count("rohit")) #print number of occurances

# li.clear() #clears complete list
# print(li)



# =============================================================

# create a list:

# thislist = ["apple", "banana", "cherry","apple"]
# print(thislist)

# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.
# print(len(thislist))

# mixed data types are allowed  : like: 

# li=[45,"rohit",97.77,True]
# print(li)

# mixede data type still have some disadvantages: 
# they cannot be sorted
# you can not find min or max element: 


# ==========================================================================

# type function:

# print(type(li))

# ===============================================================================

# the list constructor:  explicit declaration of the data type: 



li = list(("apple"," ", "banana", "cherry", 67, True, 120, "party")) # note the double round-brackets
# print(li)

# access list items:

# you can access the list using the index of the list starting from 0.

# print(li[2])

# negative  indexing: 

# print(li[-1])  # negative indexing starts from the right hand side with -1 hence -1 will represent last element

# =====================================================================================

# slicing or ranging in the list:  {) inclusive exclusive

# print(li[2:5])
# print(li[3:]) # 3 till end
# print(li[:5]) # 0 till 4th index
# print(li[:]) #complete list
# print(li[2:5:2]) #2nd till 4th index with the gap of 1 element
# print(li[2:5:]) #default is one
# print(li[::])
# print(li[-5:-2])
# print(li[-5::])

# =============================================================================================


# nested list

# nli=["rohit ", 34, [2,3,9,5,1,6]]

# # slicing: 
# print(nli[:])
# print(nli[2][2:])
# print(nli[2][3:60])
# print(nli[2][2::3])

# =========================================================================================

# if " " in li:
#     print(li)
# else:
#     print("i am good , what about you?")

# =========================================================================================

# change list items: 

# li[0]="johnny"
# print(li[0][0])
# print(li)

# # change the range of the items : 

# li[0:3]=[1,2,3]
# print(li)

# more or less than specifed range will change te length of the list  :

# ====================================================================================

# insert

# li.insert(3,"patil")
# print(li)

# append()

# li.append(100)
# print(li)

# # appending element from another list to this lsit

# app=[3,4,5,6,7,8,9]

# li.extend(app)
# print(li)

# add ANY ITERABLE: you can extend list, tuple, set, dict to list

# ======================================================================================

# removing items from the list :

# pop()emoves last item 

# basically stands for removing any element using its index

# li.pop() # this will remove from last by default
# print(li)

# li.pop(3) # removing from specified index
# print(li)

#======================================================================================

# remove : used ot remove element: remove by element no by index

# li.remove("x") # error
# li.remove(4)
# print(li)

# ========================================================================================

# removes li itself from the memory

# del li[4] #removes from index
# # del li[True] cannot delete any element
# print(li)

# del li
# error ----> print(li)
# print(li)

# ===========================================================================================

# clear(): can onlt erase the elements from the list leaving behind the empty list

# li.clear()
# print(li)

# ==========================================================================================

# looping through list 

# for x in li:
#     print(li)# list is printed len(list) number of times:

# for x in li:
#     print(x,end="||")


# # or
# print("\n")

# for i in range(len(li)):
#     print(li[i],end="//") # print i will print the indices 

# print("\n")

# j=0
# while(j is not len(li)):
#        print(li[j],end=" * ")
#        j+=1

# # short hand for loop: 

# [print(x) for x in li]

# ========================================================================================

# List Comprehension:

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# # with list comphrehension:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# # syntax:newlist = [expression for item in iterable if condition == True]

# newlist = [x for x in range(10) if x is 5]
# print(newlist)

# # expression.

# newlist = [x.upper() for x in fruits]

# # setting outcome

# newlist = ['hello' for x in fruits]

# ==================================================================================================================

# #sorting list 

# #sorting can be done in the list with the  same datatype.

# li=["true", "goa", "lion","parrot" ]
# # li.sort()
# # print(li)
# # li.reverse()
# # print(li)


# # numbers
# # you can mix floats and int as well but no strings not EVEN COMPLEX NUMBERS.

# num=[0.5,55,22.5,78.5,44]
# num.sort()
# print(num)

# li.sort(reverse=True)
# print(li)
# li.sort(reverse=False)
# print(li)

# # print(li) #sort fucntion permanantly sorts the list

# ============================================================================================================

# case insensitive sort: 
# the capiltals are sorted first than the small letters 

# li=["a","A","1"] # number strings < capitals < small letters
# li.sort()
# print(li)
# li.sort(reverse=True)

# print(li)
# li.reverse()

# print(li)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True) # ignore the capital consider them as small only
# print(thislist)


# ========================================================================================================


# copying the list:

list1=[2,3,5,1,0]
# list2=list  will make the slist2 point to the same lost that is the changes made in the list is replicated as it is the the list 2
#  copy means when there is another variable pointing towards the list having same elemests and the size but not that list with same memory address.

# so,

new=list1.copy()

print(new)


# explicit declaration 

new= list(list1)
print(new)

# =============================================================================================================

# join list
# list1=["a","b","c"]
# ==================================================================
# simple addition: 
# new_list=new+list1
# print(new_list)

# ===================================================================
# using loop

# for x in list1:
#     new.append(x)
# print(new)

# ====================================================================
# extend function

# list1.extend(new)
# print(list1)

# ==============================================================================================================

# list methods

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list











 
