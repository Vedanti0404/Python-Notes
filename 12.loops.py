# two types of loops are 

# while 
i=0
while i<=5 :
    print(i)
    i+=1
# incrementing i is important , otherwise it will be an infinite loop

# break statement:
# used to come out of loop when a specific condition is true

i=1
while i is not 5:
    print("hello")
    if i is 3:
        break
    i+=1

# continue: used to skip the entire execution for a particular iteration: 

# i=5
# while i is not 0:
#     print("hi")
#     i=i-1
#     if i is 4:
#         print("hello")
#         continue

# else statement:With the else statement we can run a block of code once when the condition no longer is true:

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
   

# ==================================================================================================

# for loop

# looping through the strings:

# string="rohit"
# for x in string:
#   print(x)

# for a in range(5):
#   print("*",end=" ")

# for i in range(2,5):
#   print(i)


for i in range(10,110,10):
  print(i)

# ===========================================================================================

for x in range(6):
  print(x)
else:
  print("Finally finished!")

  # =================================

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# Example
for x in [0, 1, 2]:
  pass

# enumearte:

for i, char in enumerate(list(range(100))):
   if(char==50):
      print(i, "is the index of 50")

for i, char in enumerate("list(range(100))"):
  print("the index is:",i,"and the character is:",char,end="\n")

# dictionary traversal:

diction = {
   "rohit":38,
   "amaya":48,
   "kshitij":11
}

# print only keys
for item in diction:
   print(item)

# print the corresponding value
for item in diction.values():
   print(item)

# print the same deafult print of the keys
for item in diction.keys():
   print(item)


# print the list of every item.
for item in diction.items():
   print(item)


# seperating the iterables of the items by storing it
for item in diction.items():
   key,value = item
   print(key,"\n", value)


# seperating the iterables of the items by storing it Second Way
for key,values in diction.items():
   print(key,"\n", values)


# while and else can go with each other
i =0 
while i<10:
   print(i)
   i+=1

else:
   print("dont with the loop!")


# while and else can go with each other if the loop is broken then the else wont work

i =0 
while i<10:
   print(i)
   i+=1
   break
else:
    print("dont with the loop!")

print("the loop is brkoen directly or not, idc")


  