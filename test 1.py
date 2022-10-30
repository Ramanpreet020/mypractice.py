#2. Given the nested if-else below, what will be the value x when the code executed successfully
x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
'''answer = 3'''

#3. What is the output of the following nested loop?
for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break
'''answer=10
          11
          12
          13'''        

#4. What is the output of the following loop
for l in 'Jhon':
   if l == 'o':
      pass
   print(l, end=", ")
'''answer= J, h, o, n '''   


#5. What is the value of x after the following nested for loop completes its execution
x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)


#6. Select which is true for for loop
#  Python’s for loop used to iterates over the items of list, tuple, dictionary, set, or string
#  else clause of for loop is executed when the loop terminates naturally
#  else clause of for loop is executed when the loop terminates abruptly
#  We use for loop when we want to perform a task indefinitely until a particular condition is met


#7. What is the output of the following if statement
a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')
'''answer = True'''  


#8. Given the nested if-else structure below, what will be the value of x after code execution completes
x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
'''answer = 2'''


#9. What is the output of the following for loop and  range() function
for num in range(-2,-5,-1):
    print(num, end=", ")
''' answer = -2, -3, -4, '''    


#11. What is the output of the following nested loop
numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
  for y in items:
    print(x, y)
''' answer =  10 Chair
              10 Table
              20 Chair
              20 Table'''    


#10. What is the value of the var after the for loop completes its execution
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)


#12. What is the output of the following range() function
for num in range(2,-5,-1):
    print(num, end=", ")
''' answer = 2, 1, 0, -1, -2, -3, -4'''    



