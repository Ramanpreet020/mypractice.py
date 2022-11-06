# FUNCTIONS MCQ

# The quiz contains 13 Questions. Solve 8 correct to pass the test.
# You will have to read all the given answers and click over the correct answer.
 
# 1. What is the output of the following function call
def fun1(name, age=20):
     print(name, age)

fun1('Emma', 25)
#  answer :Emma 25
#  Emma 20


# 2. What is the output of the following display() function call
def display(**kwargs):
     for i in kwargs:
         print(i)

display(emp="Kelly", salary=9000)
# option1. TypeError
# option2.  Kelly
#      	      9000
 
# option3. (’emp’, ‘Kelly’)
#     	    (‘salary’, 9000)
# answer : option4. emp
#    	            salary


# 3. Select which is true for Python function
#  A Python function can return only a single value
#  A function can take an unlimited number of arguments.
# answer : A Python function can return multiple values
#  Python function doesn’t return anything unless and until you add a return statement


# 4. What is the output of the following code?
def outer_fun(a, b):
     def inner_fun(c, d):
         return c + d
     return inner_fun(a, b)
res = outer_fun(5, 10)
print(res)
# answer : 15
#  Syntax Error
#  (5, 10)


# 5. What is the output of the add() function call
def add(a, b):
     return a+5, b+5

result = add(3, 2)
print(result)
#  15
#  8
# answer : (8, 7)
#  Syntax Error


# 6. What is the output of the following function call
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)
#  5
# answer : 15
#  (15, 5)
#  Syntax Error


# 7. What is the output of the following display_person() function call
# def display_person(*args):
#     for i in args:
#         print(i)

# display_person(name="Emma", age="25")
 
# anwswer: Option 1 TypeError
# Option 2 Emma
#       25
# Option 3 name
#                age


# 8. Choose the correct function declaration of  fun1() so that we can execute the following function call successfully
# fun1(25, 75, 55)
# fun1(10, 20)
# #def fun1(**kwargs)
# #  No, it is not possible in Python
# #def fun1(args*)
# def fun1(*data):

# 9. Python function always returns a value
#  False
#  True
# answer: it depends upon condition

# 10. Given the following function fun1() Please select all the correct function calls
def fun1(name, age):
    fun1("Emma", age=23)
    print(name, age)

 
# fun1("Emma", age=23)
#   2. fun1(age =23, name="Emma")
#  fun1(name="Emma", 23)
#  fun1(age =23, "Emma")


# 11. What is the output of the following function call
def fun1(num):
    print(num)
    return num + 25

fun1(5)
print(fun1)
#  25
#  5
#  answer: NameError


# 12. Select which true for Python function
#  A function is a code block that only executes when called and always returns a value.
#  answer:  A function only executes when it is called and we can reuse it in a program
#  Python doesn’t support nested function



# FUNCTIONS EXERCISE
# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.
text = "my name is {}, i am {} years old".format("john",20)
print(text)


# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.
# Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.
def fun1(x):
    print(len(x))
    return len(x)
print(fun1("200"))    


# Function call:
# # call function with 3 arguments
# func1(20, 40, 60)
def fun1():
    print("20")
    print("40")
    print("60")
print(fun1)    
fun1()   

# # call function with 2 arguments
# func1(80, 100)
# Expected Output:
# Printing values
# 20
# 40
# 60


# Printing values
# 80
# 100
def fun1():
    print("80")
    print("100")
print(fun1)    
fun1() 
 
# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
# Given:
def calculation(a, b):
    print(a+b)
    print(a-b)
    return((a+b),(a-b))  
print(calculation(40,10))        


# res = calculation(40, 10)
# print(res)
# Expected Output
# 50, 30
# Expected Output:
 
# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name,salary): 
    print("Name: " + name+" salary: "+salary)
print(show_employee("Ben","12000"))  
print(show_employee("Jessa","9000"))  


# Given:
# showEmployee("Ben", 12000)
# showEmployee("Jessa")
# Expected output:
# Name: Ben salary: 12000
# Name: Jessa salary: 9000
 
# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
def sum(a,b):
  print(a+b)

  return(a+b+5)

print(sum(40,10))        

 
# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.
# Expected Output:
# 55
def printNumber(num):
    if num:
        return num + printNumber(num - 1)
    else:
        return 0

 
# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
# Given:
# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)
# You should be able to call the same function using
# show_student(name, age)
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

show_Student = display_student

show_Student("Emma", 26)
 
# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# Expected Output:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28] 
print(list(range(4, 30, 2)))

 
# Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# Expected Output:
# 24
a = [4, 6, 8, 24, 12, 2]
print(max(a))
 


