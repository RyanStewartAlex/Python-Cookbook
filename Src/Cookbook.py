import this
import random
import sys
import os
import math
from itertools import count, cycle, repeat, takewhile, chain

'''
Resources
-------------
*Created by Ryan Stewart on September 16, 2016
*More can be found at http://www.ryanstewart.pw/

Summary: A basic cookbook for Python to reference later

Last updated: October 14, 2016
'''

#--PEP (Naming Conventions--#
#PEP: Python Enhancement Proposals
#modules should have a short, all lowercase name.
#calss names should be in CapWords style
#most variables and function names should be lowercase_with_underscores
#constats should be UPPERCASE_WITH_UNDERSCORES
#space between operators, ex: (10 + 20)



#--Prevent code from running if imported--#
if __name__ == "__main__":
	print("I am not imported")
else:
	print("I was imported")


#--Arithmetic--#
a = 10
b = 20
#addition
print(a + b)
#subtraction
print(b - a)
#multiplication
print(a * b)
#division
print(a / b)
#modulus (remainder)
print(b % a)
#exponent
print(a ** b)
#floor division (devides and rounds)
print(b // a)
#arithmetic on expressions
print("\n" * 5) #prints five new lines
#random numbers
random_num = random.randrange(0, 11)
print(random_num)


#--Strings--#
#normal
print("This is a normal string")
#Quotes inside of a string
print("\"This is quoted\"")
#multi-line quotes
print('''ThisWW
is a multi-lined
quote''')
print("This\nIs\nalso multi-lined")
#format (both work)
print("%s %s" % ("First", "Second"))
print("{} {}".format("Uno", "Dos"))
#split string into it's words
saying = "What goes around comes around.".split() #inide the parenthesis is when to split, ex: "blah.".split('.') would return ["blah", "."]
print(saying)


#--Lists--#
#assigned lists
list1 = ["hi", "this", "is", "a", "list"]
list2 = ["Well", "Hello", "There"]
print(list1[0])  #Python indexes from 0
#lists inside lists
list3 = [list1, list2]
print(list3[1][2])
#inserting new items by index
list2.insert(0, "now first item")
#inserting to end
list2.append("now at the end")
#sort alphabetically
list2.sort()
#reverse the orders of a list
list2.reverse()
#remove an object
list2.remove("Hello")
#combine contents of two lists
list4 = list1 + list2
#get amount of items in a list
print(len(list4))
#get first item in a list
print(min(list4))
#get last item in a list
print(max(list4))


#--Tuples--#
#They're lists that can't be changed
tuple1 = (1, 2, 3, 4, 5)
#change tuples by porting them to a list and back
tList = list(tuple1)
tList[0] == 100
tuple1 = tuple(tList)
#every other munipulation like len(), min(), and max() from lists work with tuples.
#tuple unpacking
tuple2 = (6, 7, 8, 9, 0)
a, b, c, d, e = tuple2
print(a)
#make one variable take the rest (ONLY PYTHON 3.0+)
'''a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)'''


#--Dictionaries--#
#defining
nick_names = {"Ryan" : "Rynoodle", "Michael" : "Hotson Mycar", "Tanner" : "Loser"}
#reading
print(nick_names["Ryan"])
print(nick_names.get("Michael"))
#get length
print(len(nick_names))


#--Sets--#
#like lists, but can't be indexed and can't contain repeating items
nums2 = {1, 2, 3, 4, 5, 6, 7}
nums3 = {81, 92, 100, 234, 31, 4, 5}
#union operator - combines two sets
print(nums2 | nums3)
#intersection operator - gets items only in both
print(nums2 & nums3)
#difference operator - gets items in the first but not in the second
print(nums2 - nums3)
#symmetric operator - gets items in either set, but not both
print(nums2 ^ nums3)


#--Conditionals--#
#if
if (1 == 1):
    print("one is equal to one")
#elseif (elif)
if (1 == 2):
    print("one is equal to two")
elif 2 == 2:
    print("one is equal to two")
#else
if (10 > 1):
    print("ten is greater than one")
else:
    print("Literally any other condition")
#and
if (10 > 10 and 10 < 1):
    print("Both conditions are true")
#or
if (10 > 1 or 5 > 1):
    print("One or both is true")
#ternary operator
b = 1 if 1 > 2 else 10 #if 1 > 2 then b is 1. Otherwise, b is 10.
print("B IS EQUAL TO " + str(b))


#--Loops--#
#for
for i in range(0, 10):
    print(i)

for x in range(5):
    print(i)

for k in [0, 1, 2, 3, 4, 5]:
    print(k)

num_list = [0, 10, 1020, 12, 0.1, 10]
for v in num_list:
    print(v)
#while
w = 0
while (w < 10):
    print("LOOPING")
    w += 1


#--Functions--#
#create a function
def my_function():
    print("Ran from my_function()")
my_function()
#create a function with arguments
def add_numbers(num1, num2):
    return (num1 + num2)
print(add_numbers(10, 300))
#function with an arbitrary number of arguments
def random_amount(arg1, *args): #*args does it
	print(arg1)
random_amount(1, 2, 3, 4, 5, 10, 100)
#functions with default values
def cookie(color, choco=True):
	print(color, choco)
print(cookie("Brown"))
print(cookie("Brown", False))
#funtions with keyword arguments
def k_test(x, y=7, *args, **kwargs): #**kwargs is what does this
	print(kwargs) #printing the kwargs returns a dictionary
k_test(1, 2, 3, a=1, b=2) 


#--Iter Tools--#
#count() counts up infinitely from a value
for num in count(3):
	print(num)
	if num > 10:
		break
#cycle() iterates through an iterable infinitely
i = 0
for ch in cycle("Ryan"):
	i += 1
	print(ch)
	if i > 15:
		break
#repeat() repeats an object either infinitely or for a number of times.
for n in repeat(17171717, 3):
	print(n)
#takewhile() takes items from an iterable while a func remains true



#--Anonymous Functions--#
'''
These are functions that don't have a name.

Why? It's a smaller way to write functions that only have one line inside.

It's in "(lambda: <var>: <var>*2)(3) format."
'''
#the example for regular functions above can be written as:
print((lambda x, y: x + y)(10, 300))
#or one that gets the sqrt of a number
print((lambda n: math.sqrt(n))(6))
#or one that cubes a number
print((lambda e: e ** 3)(7))
#can also declare it
triple = (lambda v: v * 3)
print(triple(7))


#--Map and Filter--#
#maps apply a function to an iterable
itera = range(11)
lollambda = lambda b: b ** 2
print(map(lollambda, itera))
#filters remove items from an iterable that don't match a function
nums = range(16)
isodd = lambda d: not d % 2 == 0
print(filter(isodd, nums))


#--Generators--#
#Type of iterable, but don't allow indexing. Iterated w/ for loops. Have no limit.
def my_generator():
	i = 5
	while i > 0:
		yield i #"yield" makes it a generator
		i -= 1

for i in my_generator():
	print(i)


#--Input--#
'''
b = raw_input("This is a prompt. Enter something here: ")
d = input("This is used for Python expressions. Enter something: ")
o = sys.stdin.readline()
'''


#--String Functions--#
my_string = "Hello, my guy."
#substrings
print(my_string[0:5])
print(my_string[10])
print(my_string[:-5]) #cut off the last five
print(my_string[-5:]) #leave only the last five
#find
print(my_string.find("guy"))
#get type
print(my_string.isalnum())
print(my_string.isalpha())
#get character length
print(len(my_string))
#replace
print(my_string.replace("guy", "girl"))
#remove whitespace
print(my_string.strip())
#make string a list of words
word_list = my_string.split(" ") #param is how they should be seperated
print(word_list)


#--File I/O--#
'''
#open
test_file = open("test.txt", "wb") #wb is how to write
#get info
print(test_file.mode)
print(test_file.name)
#write
test_file.write(bytes("this is being written to in bytes.", 'UTF-8'))
#close
test_file.close()
#how to read
test_file = open("test.txt", "r+") #r+ is reading and writing
text_in_file = test_file.read()
print(text_in_file)
test_file.close()
#remove file
os.remove("test.txt")
'''


#--Regex--#
'''
What is it?
	- way to search/munipulate a string based on a pattern.

I ALREADY COVERED THIS IN ANOTHER REPO, CHECK IT OUT HERE:
https://github.com/RyanStewartAlex/Python-Regex-Tutorial/blob/master/pythonregex.py
'''


#--Classes--#
#Describes what an object will be
class animal:
	mammal = True
	def __init__(self, color, legs, noise): #__init__ is the class constructor (what assigns stuff to the class)
		self.color = color #the arguments above equal to what was entered.
		self.legs = legs
		self.noise = noise

	def sayNoise(self): #all functions must take the argument "self"
		print(self.noise)

dog = animal("brown", 4, "borf")
dog.sayNoise()
print(dog.mammal)


#--Inhertiance--#
#create class
class camera:
	def __init__(self, brand, color):
		self.brand = "Generic"
		self.color = "Black"
	def sayBrand(self):
		print(self.brand)
#inherit the superclass, and make a class with it. Can make certain functions of that instance.
class DellCam(camera):
	def sayBrand(self):
		print("Dell")
	def sayGenericBrand(self):
		camera.sayBrand(self) #Could do same thing with the "super()" class

cz800 = DellCam("Dell", "Black")
cz800.sayBrand()
cz800.sayGenericBrand()


#--Magic Methods--#
#functions w/ double underscores. Also called "Dunders"
#include __init__, __add__, __mul__, __sub__ (for -),
#__truediv__, __floordiv__, __mod__, __pow__, __and__, __xor__ (for ^), __or__,
#__lt__ (for <), __le__ for (<=), __eq__, __ne__ (for !=), __gt__ (for >), __ge__,
#__len__,  __getitem__, __setitem__, __delitem__, __iter__, __contains__
class computer:
	def __init__(self, brand): #__init__ and __add__ are both magic methods.
		self.brand = brand

	def __add__(self, other): #Called when an instance of computer is added
		return(other.brand)

comp1 = computer("Dell")
comp2 = computer("Alienware")
print(comp1 + comp2)

#another example
class makeList():
	def __init__(self, cont):
		self.cont = cont 

	def __len__(self):
		return 0 #will always return 0, doesn't matter how much there actually are.

	def __getitem__(self, index):
		return "Your index was: " + str(index)

l = makeList([0, 1, 2, 3, 4, 5])
print(len(l))
print(l[1])


#--Encapsulation (data hiding)--#
#private methods prevent other classes from accessing that info
#Most language completely make classes private, but Python it's still possible to get to private classes with outside classes.
class keyboard:

	__language = "Svenska"

	def __init__(self, maker): 
		self._hiddenMaker = maker #weakly private Python functions are denoted with '_' before the class

	def setMaker(self, other):
		self._hiddenMaker = other

	def getMaker(self):
		return self._hiddenMaker

	def setLanguage(self, other):
		self.__language = other

	def getLanguage(self):
		return self.__language

rgb = keyboard("Corsair")
print(rgb.getMaker())
print(rgb._hiddenMaker) #Can still get b/c it's weakly private
print(rgb.getLanguage())
#print(rgb.__language) (can't get b/c strongly private)


#--Class Methods--#
#classes inside classes that take diff arguments
class rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def getArea(self):
		return self.width * self.height

	@classmethod #class methods prefixed with the @classmethod decorator
	def square(cls, sideLength):
		return cls(sideLength, sideLength)

	@staticmethod #static methods are like regular functions, except than can belong to an instance. Don't require any additional arguments.
	def colorList(colors):
		for color in colors: #generator
			yield color

square1 = rectangle.square(10)
print(square1.getArea())
#Read from a generator
c = rectangle.colorList(["Yellow", "Orange", "Blue"])
for generated in c:
	print(generated)


#--Freeing Memory--#
a = 12
del a #automatically deleted if a were to reach 0


#--Properties--#
#Create attributes to an object
#requires the "@property" decorator
class pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@property
	def meatLoversAllowed(self):
		return False

	@meatLoversAllowed.setter
	def meatLoversAllowed(self, x):
		self.meatLoversAllowed = self.x

p1 = pizza(["Meat", "Pineapple", "Peperoni"])
print(p1.meatLoversAllowed)
p1.meatLoversAllowed = True
print(p1.meatLoversAllowed)


#--Major External Libraries--#
#Django for web framework (Instagram and Disqus uses it)
#BeautifulSoup for web scraping
#Matplotlib to make graphs from data in Python
#NumPy for multidimensional arrays instead of nested lists
#Panda3D for 3D games.
#Pygame for 2D games.


#--Packaging--#
'''
What is it?
	- putting modules in standard form for distribution
	- First, organize your files correctly
		- Put all files in the same directory
		- Put an __init__.py file in the same directory (doesn't matter if empty or not)
		- Put that directory in a new directory with the README, licensing info, and setup.py
		- An example would be:
			MyProgram/
				LICENSE.txt
				README.txt
				setup.py
				myprogram/
					__init__.py
					firstfile.py
					secondfile.py

	- setup the "setup.py" file.
		- an example would be:
			from distutils.core import setup

			setup(
				name='MyProgram'
				version='0.1dev'
				packages=['MyProgram']
				license='MIT'
				long_description=open('README.txt').read()
			)

	- Upload your packaged program to PyPI or use CMD to greate a binary distribution (installer)
		- To create a binary distribution in CMD:
			- go to the directory with the setup.py
			- run "python setup.py sdist"
			- run "python setup.py bdist_wininst"
