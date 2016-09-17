import random
import sys
import os

'''
Resources
-------------
*Created by Ryan Stewart September 16th, 2016
*More can be found at http://www.ryanstewart.tk

Summary: A basic cookbook for Python to reference later

What it covers:
    - Arithmetic
    - Strings
    - Lists (Arrays)
    - Tuples
    - Dictionary
    - Conditionals
    - Loops
    - Functions
    - User input
    - String functions
    - File I/O
    - Classes and Objects
    - Constructors
    - Inheritance
    - Overwriting functions
    - Overloading functions
    - Polymorphism
'''


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
print('''This
is a multi-lined
quote''')
print("This\nIs\nalso multi-lined")
#format (either work)
print("%s %s" % ("First", "Second"))
print("{} {}".format("Uno", "Dos"))


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


#--Dictionaries--#
#defining
nick_names = {"Ryan" : "Rynoodle", "Michael" : "Hotson Mycar", "Tanner" : "Loser"}
#reading
print(nick_names["Ryan"])
print(nick_names.get("Michael"))
#get length
print(len(nick_names))


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


#--Classes / Objects--#
#declaring
class Animal:
    __name = "" #underscores mean it's private and therefor needs a method in side to set them
    __height = 0
    __weight = 0
    __sound = ""

    def __init__(self, name, height, weight, sound): #constuctor
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name): #encapsulation
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                      self.__height,
                                                                      self.__weight,
                                                                      self.__sound)

#create object
cat = Animal("Canned Food Kitty", 33, 100, "Meow")
print(cat.toString())


#--Inheritance--#
class Dog(Animal): #creates dog class with everything from animal class
    __owner = ""

    def __init__(self, name, height, weight, sound, owner): #overwrite constructor
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.__name,
                                                                      self.__height,
                                                                      self.__weight,
                                                                      self.__sound,
                                                                      self.__owner)

    #--Overloading--#
    def multiple_sounds(self, how_many=None): #attributes set to "None" can be set or not
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

#create object spot of the dog class
spot = Dog("Spot", 40, 100, "Chris")
print(spot.toString())


#--Polymorphism--#
'''
What does it mean?
    - automatically call the correct functions based on data type
    ex: call the same function with a string, int, float, or double.
'''

class AnimalTesting:
    def get_type(self, Animal):
        Animal.get_type()

test_animals = AnimalTesting()
test_animals.get_type(cat) #prints "Animal"
test_animals.get_type(spot) #prints "Dog"

spot.multiple_sounds(4)
spot.multiple_sounds()