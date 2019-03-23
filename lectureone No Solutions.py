#this is a comment. Try to code without using many comments

print "Hello Word!" # This is a basic print statement. It writes to the console

# Curriculum: boolean logic, control statements (while, for, if), tuples, recursion, functions, strings, arrays (lists) 
# input, output, -> Calculator? Battleship?

# basic arithmetic: 

x = 1
print x

x = x + 5
print x

x = x - 2
print x

x = x*3
print x

x = x / 6
print x

# We will now start with boolean logic:
# A Boolean is a value which is either true or false. We can write statements which are either true or false

x = False
print x

print False == True # the "==" operator is used to compare values (more on this later on)

print False == False

print False is True # can also use "is"

print True is True

print True is not True # not is negation in logic

print True or not True # or is like || in boolean logic (or)

print False or not False

print True and False

print True and not True

print True == (not False) # use parentheses for order of operations here

print 3 > 4 # greater than

print 5 >= 3 # greater than or equal to

print 5 > 3 or 5 == 3 

print 3 < 2

print (((False and True) or (True and False)) and False) or True #paying attention?


# Now Control Statments

if (True):
	print "Hello World!"
else:
	print "Goodbye World!"

x = 1

if (x == 2):
	print "hi"
elif (x == 3):
	print "bye"
else:
	print "good afternoon"

for x in range (1, 5): # print 1 through 4
	print x

for x in range(5): # print 0 through 4 because computer scientists count with 0 first
	print x

for x in range(10):
	print x * 2 

print 3**3 # exponent

print 3 ** 4 # 3^4


x = 15
while (x > 10):
	print x
	x = x - 1

x = (1, 2, 3)
print x
print x[0]
print x[1] # 2

x = x + (4, 5)
print x

print x[-1] # the last number in tuple
print x[-2] # the second last number in tuple

y = ("cat", "dog", "mouse") #tuple of strings
print y
print y[-1]

y = ("cat", "dog", "mouse", 2, 3.14) # can mix types
print y

print y[-2]


# Functions

def fact(n): # recursive factorial
	if (n == 1):
		return 1
	return n * fact(n-1)

print fact(5)

def factn(n): #non recursive factorial
	sum = 1
	while (n >= 1):
		sum = sum * n
		n = n - 1
	return sum

print factn(5)


# Strings
# Keep in mind that Python strings are immutable! (you can't change them!)

s = "hello"
x = s.find("l") # find() looks for a string within a string, and returns its position if found. It returns -1 if not found!
print x

x = s.find("y") # find() is the same as index(), except index does not return -1 if not found, it returns an exception
print x

print len(s) #length of string

print s[1]

print s[0:3] # up to but not including the character in position 3 (4th character because we count from 0)

v = " world!"

x = s + v # combine strings
print x

x = v + s 
print x

# how to flip first and last characters of a string? (and return it as a new string)


# LEAK THE ANSWER


answer = s[-1] + s[1:-1] + s[0]
print answer


# Arrays (lists) 
# Arrays are mutable

x = [] # empty list
print x

x = [1] #one element list 
print x

x = [1, 2, 3, 4, 5] # 5 element list
print x

x = [0] + x # [0, 1, 2, 3, 4, 5]
print x

print x[3]

x[3] = 1 # Array's ARE mutable!
print x

x[3] = 3

squares = [y**2 for y in range(0, 6)] # Combine what we've learned so far! if you use x here, it will get changed
print squares

print x == [z for z in range(0,6)]

print x[3:] #position 3 and onward
print x[:3] #up until position 3
print x[1:3] #range from 1 up until 3

print x[-2:] # second to last position and onwards
print x[:-1] # up until last element

print len(x) # can print the length of an array

index = 3
element = 16
x.insert(index, element) # insert the specified element into the specified index
print x

print x.pop() # remove the last element of the array, (and return it as a value!)
print x

print x.pop(1) # pop has an optional argument for the index to "pop"
print x

print x.count(1) # count() prints the number of times the specified element appears in the array

x = x + [1, 2, 3, 1, 1, 2, 3]
print x
print x.count(1)

x.sort() # sorts in increasing order from left to right
print x

y = ["Python", "is", "fun"] 
y.sort() # by default, python will sort using the < operator. Read the docs if you are curious about this
print y

print "Python" < "fun" # read about Ascii to find out why this is the case. Hint: Capital letters come before lowercase
print "fun" < "is"

x.reverse()
print x


# Input/Output

x = input("Enter a string: ") #read into validating input if you are curious about this
print x

x = input("enter a number: ")
print x

# can you make a calculator now?

# what about battleship?