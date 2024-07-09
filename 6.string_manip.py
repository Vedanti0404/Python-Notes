# x=input("enter a string: ")
# print(x)

# accessing characters is possible: but changing it is not : 
# print(x[5])

# x[5]="r"
# print(x)

# multiline string:
# with """ or '''
# in the result, the line breaks are inserted at the same position as in the code.


# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# looping throught he string: 

# for x in "banana":
#   print(x+ " ")

# finding the lrngth of the string  

# print(len(x))



# operation on strings :

#1) Slicing : [{:)]

# print(x[4])

# print(x[0:5])

# print(x[5:])#till the complete string is printed from inclusive index

# print(x[:7])#from the beggining till the exclusive index

# print(x[4:8])

# print(len(x))

# print(x[:])

# print(x[:90])#stop till the end only

# print(x[::2])#gap of 2

# print (x[::])# (0:0:1)

# print(x[-7:-1])

# print(x[::-1])#reverse a string

# print(x[-9:-4:-2])

#2)string functions:

# a="Rohit is a good boy."
# print(a.casefold())

# print(a.center(35)) #table formmating 

# print(a.encode())

# print(a.endswith("."))

# print(a.isascii()) #return true if all the values are ascii values: 

# ac="456"
# print(ac.isdecimal())

# print(type(x))

# print(x.isalnum()) #if spaces then false

# print(x.isalpha()) #is alphabetic , if spaces then false

# print(x.isspace())#true if all white spaces

# print(x.endswith("l"))

# print(x.count("i"))

# print(x.capitalize())#first letter

# print(x.find("i"))#roh before first occurance of i so returns 3

# print(x.upper())

# print(x.lower())

# print(x.replace("i","o")) #all te occurances are replaced

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# a = "Hello, World!"
# print(a.replace("Hello", "J"))

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# # works just like: 
# txt = "My name is John, and I am "
# print(txt,age)


# # but the advantage is here: 
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))
 

#  escape characeter: 
# \n : line 
# \t : tab
# \"\": to print (" ") in the print function 
# \\ : to print \ in the print function




# ==============================

# checking in string: 
# txt = "The best things in life are free!"
# print("free" in txt) # gives boolean as result: 


# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" not in txt) #bollean result 

# |=====================================================|
# |------------------ ALL FUNCTIONS --------------------|
# |.....................................................|

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



