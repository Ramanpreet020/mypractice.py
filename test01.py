 
 
# Solve these Questions using loops and recursion
 
# 1.	Find Sum of numbers from 1 to n 
# find out the sum of numbers from 1 to n like 1 + 2 + 3 + 4 +, etc
# p=int(input())
# sum = p*(p+1)/2
# print(sum)
    

# 2.	Reverse a string 
# a=str(input())
# b=a[::-1]
# print(b)

# 3. Adding all numbers in a list 
# d=[1,2,3,4,5,6]
# print(sum(d))


# Python Practice Questions

# 1.# we need to write a python program to find the power of a number using recursion
# input : num = 2, power= 3
# # output : 8
# a=int(input("num : "))
# b=int(input('power : '))
# p=a**b
# print(p)

# 2.Assign a different name to function and call it through the new name
# def my_function(name):
#     print(name)

# my_function("preeti")
 
# 3.Python Program to Print All Odd Numbers in a Range
# n=int(input())
# if n%2==0:
#     print("its an even number")
# else:
#     print("its an odd number ")
    

# 4.Python Program to Check Whether a Given Number is Even or Odd using Recursion
# def check(n):
#     print(n)
#     return(n%2==0)
# n=int(input("Enter number:"))
# if n%2==0:
#       print("Number is even!")
# else:
#       print("Number is odd!")


# 5.Python Program to Check whether a Number is Prime or Not using Recursion
# def Prime_Number(n, i=2):
#     if n == i:
#         return True
#     elif n % i == 0:
#         return False
#     return Prime_Number(n, i + 1)


# n = int(input())
# if Prime_Number(n):
#     print("Yes,", n, "is Prime")
# else:
#     print("No,", n, "is not a Prime")


# 6.Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3
# n= int(input())
# if n%2!=0 or n%3==0:
#     print(n)
# else:
#     print("number is divisible by 2 and 3 ")


# 7.Python Program to Check if a Number is a Palindrome
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")


# 8.Python Program to Count the Number of Vowels in a String
# string = str(input("Enter string:"))
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)

# 9.Python Program to Remove Odd Indexed Characters in a string
# def odd_values_string(str):
#   result = "" 
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result

# print(odd_values_string('abcdef'))
# print(odd_values_string('python'))

# 10.Python Program to Remove the nth Index Character from a Non-Empty String
# def remove_char(str, n):
#       first_part = str[:n] 
#       last_part = str[n+1:]
#       return first_part + last_part
# print(remove_char('Python', 0))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))

# 11.Python Program to Replace Every Blank Space with Hyphen in a String
# string=str(input("Enter string:"))
# string=string.replace(' ','-')
# print("Modified string:")
# print(string)


# 12.Python Program to Calculate the Length of a String Without using Library Functions
# s= str(input())
# z=len(s)
# print("lenght of the string: ",z)

# 13. Python Program to Count Number of Lowercase Characters in a String
# string=str(input("Enter string:"))
# count=0
# for i in string:
#       if(i.islower()):
#             count=count+1
# print("The number of lowercase characters is: ")
# print(count)


# 14.Python Program to Count the Number of Vowels in a String
#done in question number 8

# 15.Python Program to Count Number of Uppercase and Lowercase Letters in a String
# string=str(input("Enter string:"))
# count=0
# for i in string:
#       if(i.islower()) and (i.isupper()):
#             count=count+1
# print("The number of lowercase characters is: ")
# print(count)


# 16.Python Program to Find Common Characters in Two Strings
s1=str(input("Enter first string:"))
s2=str(input("Enter second string:"))
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)


# 17.String Palindrome Program in Python

# my_str = 'aIbohPhoBiA'

# # make it suitable for caseless comparison
# my_str = my_str.casefold()

# # reverse the string
# rev_str = reversed(my_str)

# # check if the string is equal to its reverse
# if list(my_str) == list(rev_str):
#    print("The string is a palindrome.")
# else:
#    print("The string is not a palindrome.")

# 18.Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string=str(input("Enter string:"))
ch=str(input("Enter character to check:"))
print("Count is:")
print(check(string,ch))








