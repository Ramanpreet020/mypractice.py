#if-else condition
# some imp logical operator
'''if (condition):
    code if coondition is true''' 
if(20 > 30):
    print("20 is greater than 30")
x = 20 
y = 10 
if(x>y):
    print("x is greater than y")
else:
    print("x is equal to or equal to y")

collegeENTRYTime = 9 
studentENTERTime = 9
if(studentENTERTime<collegeENTRYTime):
    print("you can enter in the college")
elif(studentENTERTime==collegeENTRYTime):
    print("you can enter with late remark")
elif(studentENTERTime>12):
    print("aloweeded to enter with proper felicitation")    
else:
    print("you can go back to your respective residences or hostels")
#and(&) and or
x = 10 
y = 20
z = 30
if(x<y and x<z):# only if both conditions are true 
    print("x is lesser than all ")
if(x<y or x<z):#atleast one is true
    print("x is smaller than all ")    

# NESTED CONDITION
#one condition inside another
age = 20
if(age<18):
    print("age is less than 18")
    if(age<10):
        print("the person is minor,no entry")
    else:#range for this is 10 to 17
         print("the person is allowded")    
else:
    print("age is greater than or equal to 18 ")












