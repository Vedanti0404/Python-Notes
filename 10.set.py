# #set: property of a set is to store unique values


# # print(type(s))
# s=set([1,2,3,4,5,6,6,10,11,12,13])

# # l=[1,2,3,4,5,6]
# # print(set(l)) #please note that set is now containing duplicate 6 but printed only once.
# # s=set([l])

# print(s)

# s.union({1,2,3,4,5,100})
# print(s)

# s.intersection({1,2,3,4})
# # s.add(10)
# print(s)

# print(max(s))

# # set is a union 

# =========================================================================================

# sets : unordered , unchangeable , and DOES NOT ALLOW UNIQUE CHARACTER

# sets items are unmodifiable but you can add the items to a set adn similarly remove from the set

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# always print the different order:

# stores unique value:

# thisset = {"apple", "banana", "cherry","apple"}
# print(thisset)

# ===========================================================================================

# length of the set:

# print(len(thisset))

# ============================================================================================

# type function:

# print(type(thisset))

# =======================================================================================
# sets can have different type mixed datat type: 

# set constructor or explicit declaration:

# st=set(("rohit ", 34, 89.9, True))

# print(st)

# ==========================================================================================

# accessing the set elements:

# you cannot access the set with reffering to the index or key.

# looping through set.

# for i in thisset:
#     print(i)

# # check if the element in present in that set:

# if "banana" in thisset:
#     print("true")

# print("banana" in thisset)

#=============================================================================================

# adding element to the set: 

# add(): appends the element default:

# thisset.add("rohit")
# print(thisset)

# ===========================================================================================

# update(): add set to the set.
# st={1,2,3,4}

# thisset.update(st)

# print(thisset)

# you can add any iterable, like list, dictionary, tuple

# ============================================================================================

# remove items

# thisset.remove("rohit")
# print(thisset)

# thisset.discard("rohit")
# print(thisset)


# thisset.remove("rohit")
# print(thisset)

# both the discard and the remove works the same n=butm the discard wont show any error if the element is not there but print the same set again , on the other side the remove will show an error.

# pop():

# thisset = {"apple", "banana", "cherry"}

# x=thisset.pop()

# print(x)

# # or thisset.pop() is also fine

# print(thisset)

# some points to remember:

# 1) we cannot access any item using its index as the set is unorederd

# 2)similarly we cannot say which in pop() will be removed as any element can be at last index

# ============================================================================================

# clear(): empty set

# thisset.clear()
# print(thisset)

# ========================================================================================

# del thisset # completely removes the set

# ======================================================================================

# thisset = {"apple", "banana", "cherry","apple"}
# print(thisset)

# for x in thisset:
#     print(x)

# =========================================================================================

# join sets:

# union(): this set will return new set so needs to store in the variable:

set1={1,2,3}
set2={"a","b","c"}
# setr= set1.union(set2)
# print(setr)

# ====================================================================================

# update() will update any one of the sets hence dont need any new variable:

# set1.update(set2)

# print(set1)

# both will exclude the duplicates

# ====================================================================================

# keep only the duplicates:


# intersection_update() will update the current list and will keep onky the repeating elements
# set1.intersection_update(set2)
# print(set1)

# ==========================================================================================

# intersectio()  will do the same but needs variable like union

# setr=set1.intersection(set2)
# print(setr) #empty set

# ======================================================================================

# keep all but not the same elements:

# symmetric_differene_update(): just like update and intersection_update it will show all those which are not common in the current set.

# set1.symmetric_difference_update(set2)
# print(set1)

# =========================================================================================

# symmetric_difference : needs an variable to store the not common elements:

# setr=set1.symmetric_difference(set2)
# print(setr)

# ========================================================================================

# set methods: 
# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

# ========================================================================================










