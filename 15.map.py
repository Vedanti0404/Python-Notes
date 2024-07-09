# map is the pure function that takes a function call and the data to be acted upon and pases the copy of the data to be acted upon .and then return the result
my_list = [1,2,3]
def return_muliplied(item):
    return item*2

print(list(map(return_muliplied, my_list)))
print(my_list)

# filter
# filter is used to create a list of items from all the iterables whcih gives the value TRUE only.

def check_odd(item):
    return item%2!=0 # will return tru for the numbers which are odd.  

print(list(filter(check_odd,my_list)))
print(my_list)


# zip 
# zip function is used to zip the 2 or more funcitons together.
list_2 = [1,2,4]

print(list(zip(my_list,list_2)))


# reduce

from functools import reduce
def accum(acc,item):
    print(acc, item)
    return acc+item

print(reduce(accum, my_list, 0))