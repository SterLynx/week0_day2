# day 2 lesson notes, Python
# this is a comment in python it can be used in one line or multiple lines, or even after a line

integer1 = 5 # this is a variable named integer1 that we have assigned the value of 5

# show float data type
float1 = 5.0

# math operations

# add +

added = 4 + 4
print(added)

# subtract -

subs = 10 - 5
print(subs)

# multiply *

prod = 5 * 10
print(prod)

# divide /
# always results in a float (number with a decimal)

div = 10 / 2
print(div)

# floor division //
# results in an integer
floor = 7 // 2
print(floor)

# modulo %
# gives us the remainder
# rem helps determining odd vs even numbers. Prints a boolean of 1 or 0, true or false
rem = 7 % 2
print(rem)

# exponent **
power = 2 ** 3
print(power)

# = vs ==
# = makes something equal to, meaning it assigns the value of a given integer such a x = 3 or number = 10. == on the other hand checks if something is true 

# strings
stringy = 'Any kind of characters inside of quotes'
# strings are iterable, immuteable, ordered
print(stringy[4]) # the brackets denote which letter in the string is printed, including the spaces (if they exist)

stringy1 = 'This'
stringy2 = 'is'
stringy3 = 'not'
stringy4 = 'one word!'

add_str = stringy1 + stringy2 + stringy3 + stringy4 # Concatonation 
print(add_str)

add_str2 = add_str + ' Here\'s another sentence added to the string!'
print(add_str2)

#interpolation 

f_exp = f"This is just another string but we can throw in a python variable here --> {integer1}"
print(f_exp)

# lists
# lists are ordered, mutable, dynamic, iterable
alist = []
alist2 = [1, 2, 3, 4]
# stuff in the list is basically hidden, python knows the length but not the contents until you specificially call it

# functions vs methods 
# functions can be called from anywhere, methods are for a specific object or class .append(), .pop(), and .remove()
# methods have a . before their name

# example 
# .append() adds an item to the end of the list
alist2.append(4)
print(alist2)

# .pop() takes the last element out of the list

popped = alist2.pop(4)
print(alist2)
print(popped)

# .remove() find the first occurence of the value and removes it from the list

alist2.remove(4)
print(alist2)

alist2.append(4)
alist2.append(5)
print(alist2)

print('range demo \n\n')
print(list(range(11))) # it starts with 0 by default, if it was 10 it would print 0 - 9, with 11 it prints 0 - 10
# to edit the range is print(list(range(1,11, 5)))

# range - returns a sequence of numbers STARTING FROM 0 by default, and increments of 1 by default, and stops BEFORE a specified number
# parameter values, you can set the start, stop, and step of the range

numbers = list(range(5, 15))

# loops in python
# for loop

#   syntax --> for item in items:
for num in numbers:
    wanted_num = num * 10
    print(wanted_num)

# index loop
for i in range (len(numbers)):
    print(i, numbers[i])

# while loop 
    # loops while a condition is true

while True:
    print("Crazy? I was crazy once. They locked me in a room. A rubber room! A rubber room with rats, and rats make me crazy.")
    break

# while counter

counter = 0
while counter < 10:
    print(counter)
    counter += 1 # += adds, *= multiplies, -= subtracts

# pointers 

l = 0
r = len(numbers)-1
while l < r:
    print(l)
    l += 1

print('\nMembershipchecks:\n')

name_list = ['William,' 'Zachary', 'Andrew']
# member checks, is this a value in the list? 
print("Andrew" in name_list)
print("Jack" in name_list)
print('back' in 'back to the future')
print ('front' in 'back to the future')

# conditionals
# if/elif/else
# the bottom example checks the ages of potential voters, given an age it will calculate what voting age the person is
# the if/elif/else will always start with "if", if it has "elif" it will always be before "else" 

age = 20

if age >= 65:
    print("you're a senior")
elif age < 18:
    print("you're a kid")
else:
    print("you're an adult")

# and / or
# truth tree
# true and true --> true
# true and false --> false
# false and false --> false

# true or true --> true
# true or false --> true
# false or false --> false

if age < 66 and age > 18:
    print('I told ya it was an adult')

#functions - self defined stuff 

#def plusfive(num):
    #print (num + 5)

def timesfive(num):
    print(num * 5)

timesfive(1)

# because timesfive has a value (1) it prints fine, but plusfive does not have a value which is why it prints as none

#return vs print 

# inputs
#x = int(input('what would you like to type?'))
#print(x,type(x))



# turning the previous example into a function

def ageism(agenumber):
    if agenumber > 64:
        print("you're a senior")
    elif agenumber < 18:
        print("you're a kid")
    else:
        print("you're an adult")

y = int(input('input an age\n'))
ageism(y)
























#TO-DO : RANGE FUNC