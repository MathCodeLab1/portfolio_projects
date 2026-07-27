


# ===============================================================================================
# =================================== Exercise 3.1 ==============================================

# === The original program (correct version) ===

def print_lyrics():
    print ("I 'm a lumberjack, and I 'm okay.")
    print ("I  sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()




# == Move the function to the top and see what happen ==

repeat_lyrics()

def print_lyrics():
    print ("I 'm a lumberjack, and I 'm okay.")
    print ("I  sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# NameError : name 'repeat_lyrics' is not defined
# Reason: The function is called before it is defined.


# =============================================================================================
# =================================== Exercise 3.2 ============================================



# == Move the call to the bottom and change the order of the function ===

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("T 'm a lumberjack, and I 'm okay.")
    print("I sleep all night and I work all day.")

repeat_lyrics()

# == What happens ==
# == The program works correctly and prints the lyrics twice.

# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.

# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.


# == Why does it works ==
# == Because Python reads the file first and creates both functions before the call happens.

# == Execution order:
	# 1.	Define repeat_lyrics
	# 2.	Define print_lyrics
	# 3.	Run repeat_lyrics()
	# 4.	repeat_lyrics() calls print_lyrics()


# So everything exists when it is needed.

# == Key idea to remember

# == Python executes code top → bottom.

# == But functions can call other functions as long as they are defined before the call happens.



# ===============================================================================================
# ===================================== Exercise 3.3 ============================================



# Python provides a built-in function called len that returns the length of a string, so
# the value of len('allen') is 5.
# Write a function named right_justify that takes a string named s as a parameter and prints the
# string with enough leading spaces so that the last letter of the string is in column 70 of the display.
# >>> right_justify('allen')


def right_justify(s):
    spaces = 70 - len(s)
    print(" " * spaces + s)

print("allen")




# ===================================================================================================
# ======================================  Exercise 3.4  =============================================


#  A function object is a value you can assign to a variable or pass as an argument. For
#  example, do_twice is a function that takes a function object as an argument and calls it twice:
#  def do_twice(f):
#  f()
#  f()
#  Here’s an example that uses do_twice to call a function named print_spam twice.
#  def print_spam():
#  print 'spam'
#  do_twice (print_spam)
#  1. Type this example into a script and test it.
#  2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
#  function twice, passing the value as an argument.
#  3. Write a more general version of print_spam, called print_twice, that takes a string as a
#  parameter and prints it twice.
#  4. Use the modified version of do_twice to call print_twice twice, passing'spam' as an
#  argument.
#  5. Define a new function called do_four that takes a function object and a value and calls the
#  function four times, passing the value as a parameter. There should be only two statements in
#  the body of this function, not four.


#  Step 1 - given code

def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")

do_twice(print_spam)


# Step 2 - Modify do_twice

# Now the function must take:

#  a function

#  b value

def do_twice(f, value):
    f(value)
    f(value)


# Step 3 - Create prnit_twice

def print_twice(s):
    print(s)
    print(s)

# Step 4 Call print_twice

do_twice(print_twice, "spam")


#  Explanation :

#  do_twice calls print_twice two times print_twice prints spam two times
#  2 * 2 = 4 prints.

# Step 5 - Create do_four

#  We reuse do_twice.

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

# do_four(print_twice, "spam")


# =====================================================================================
# ===============================  Exercise 3.5 =======================================


#  This exercise can be done using only the statements and other features we have learned
#  so far.
#  1. Write a function that draws a grid like the following:





+ - - - - + - - - - +
| | |
| | |
| | |
| | |
+ - - - - + - - - - +
| | |
| | |
| | |
| | |
+ - - - - + - - - - +



# Hint: to print more than one value on a line, you can print a comma-separated sequence:
# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the value printed
# next appears on the same line.
# print '+',
# print '-'
# The output of these statements is'+ -'
# .
# A print statement all by itself ends the current line and goes to the next line.
# 2. Write a function that draws a similar grid with four rows and four columns.
# Solution: http: // thinkpython. com/ code/ grid. py . Credit: This exercise is based on an
# exercise in Oualline, Practical C Programming, Third Edition, O’Reilly Media, 1997.
   

# ==================================================================================================

# Exercise 6.1. Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
    
print(compare(5, 3)) # 1
print(compare(3, 3)) # 0
print(compare(2, 5)) # -1


# =====================================================================================================

# Exercise 6.2. Use incremental development to write a function called hypotenuse that returns the
# length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record
# each stage of the development process as you go.

import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print(hypotenuse(3, 4))

# ==== Mini Project - Cooking Time Calculator ===

# Problem

# You are cooking and want to calculate:

# 1️⃣ Preparation time
# 2️⃣ Cooking time
# 3️⃣ Total time

# ⸻

# Step 1 — Write the functions

# 1. Preparation time

# Each ingredient takes 3 minutes to prepare.

def preparation_time(ingredients):
    return ingredients * 3


# 2. Cooking time

# Cooking takes 10 minutes per item

def cooking_time(items):
    return items * 10


# 3. Total time

def total_time(ingredients, items):
    return preparation_time(ingredients) + cooking_time(items)

print(total_time(4, 2))


# =========================================================================

# Exercise 6.3. Write a function is_between(x, y, z) that returns True if x ≤y ≤z or False
# otherwise.

def is_between(x, y, z):

    return x <= y <= z

result = is_between(3, 4, 5)
print(result)
