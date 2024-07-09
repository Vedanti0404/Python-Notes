# # li=[]
# # print(type(li))
# # tp=()
# # print(type(tp))
# # di={}
# # print(type(di))

# di={"rohit": "patil", "sarthak":69,48:"amaya"}

# # print(di["rohit"])
# # print(di[48])
# # print(di["sarthak"])

# # numbers can be assigned to string and vice versa

# # operations to add in dictionary:

# # di.update("vedant":40) # will be appended at last
# # print(di)

# # di["new_diction"]={"Rohit":"yotube","fool":420}
# # print(di)
# # print(di["new_diction"]["Rohit"])
# # del di["sarthak"]
# # print(di)
# # print(len(di))


# # copy function: which makes a copy of the original function:

# # d3=d2 here any changes in d3 will be reflected in d2 also and vice versa

# # but 

# print(di.copy())

# print(di.get("rohit")) #get the value of the key 

# print(di.items()) #prints pair of key with it's element

# print(di.keys()) #print the keys of the dictionary

# # di.pop("new_diction")
# # print(di) #remove last element

# print(di.values())#will print the values of all keys

# print(di.clear()) #clear the dictionary



# ========================================================================================

# dictionaries:

# ordered :When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# changeable:Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# do not allow duplicaates: Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
# print(thisdict)

# =======================================================================================

# the elements can be refered by their elements key name:

# ========================================================================================

# print(len(thisdict))
# print(type(thisdict))

# can allow mixed key and vale combinations:

# ========================================================================================

# accessing th elements: 

# print(thisdict["brand"])

# =========================================================================================

# get():

# print(thisdict.get("brand"))

# ==========================================================================================

# get all the keys printed using: key()

# print(thisdict.keys())

# ==========================================================================================

# get all the values printed using : values()

# print(thisdict.values())

# ==========================================================================================

# get the key and it's value printed in the pair: items()

# print(thisdict.items())

# =========================================================================================

# change an item :

# thisdict["brand"]="BMW"

# print(thisdict)

# ===========================================================================================

# check if the KEY exist

# print("brand" in thisdict)


# ============================================================================================


# chaning the dictionary
# update():

# thisdict.update({"rohit":38})
# print(thisdict)

# ============================================================================================

# removing dictionary items: 

# pop(key_name) : here the pop will remove the specified key only

# thisdict.pop("rohit")
# print(thisdict)

# =========================================================================================

# to remove the last element: use popitem()

# thisdict.popitem()
# print(thisdict)

# ==========================================================================================
# # delete an key
# del thisdict["brand"]
# print(thisdict)

# ============================================================================================

# to remove complete dictionary:

# del thisdict

# ===========================================================================================

# clear():  will print the empty dictionary

# =========================================================================================

print(thisdict)

# loop through dictionary:

# for x in thisdict:
#   print(x)

# this will print only the keys:


# but particularly only keys:
# for x in thisdict.keys():
#   print(x)

# ===========================================================================================

# for x in thisdict:
#   print(thisdict[x])

# prints values only

# but particularly: only values

# for x in thisdict.values():
#   print(x)

# ===========================================================================================

# print both the key and the values

# for x, y in thisdict.items():
#   print(x, y)

# ==========================================================================================

# copy dictionary:

# thisdict2=thisdict is not an option cause it will point to the same dictionary and any changes made in thisdict will be reflected in thisdict2 also.

# so

# new=thisdict.copy()

# print(new)

# =========================================================================================

# another way is to make the explicit decalration

# new=dict(thisdict)

# print(new)

# ============================================================================================

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# ==========================================================================================

# methods:
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

