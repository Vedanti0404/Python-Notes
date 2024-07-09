# list comprehension are used to make the list of the following variables that follow the conditon that too in the smalles possible way.

#  make the list of tnhe vowels from the sentence;

sentence = "hello, my name is Rohit"

# tradional way.
lists = []
for char in sentence:
    if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        lists.append(char)

print(lists)

# make a list of the numbers in the range from 1 to 100 the numbers which are divisible by 7
lists = []
for i in range(1,106):
    if(i%7==0):
        lists.append(i)

print(lists)

# now using the list comprehensions

list_c = [char for char in sentence  if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u')]
print(list_c)

list_c = [num for num in range(1,106) if(num%7==0)]
print(list_c)

# if we just ,make a set of it then it becomes a set


list_c = {char for char in sentence  if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u')}
print(list_c) #set is created