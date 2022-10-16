#python operater 

print(8+3) #additon 
print(8-3) #subtraction
print(8/3) #division
print(8%3) #modulation
print(8*3) #multiplying
print(15//6)  #gives only integer quotient 
print(8**3) #act as power i.e. 8^3

#2..assignment operators

a = 3 #assign value 3 to a
print(a)
a+=5 #same as a=a+5
print(a)
a-=5 #same as a=a-5
print(a)
a*=3 #same as a=a*3
print(a)
a/=4 #same as a=a/4
print(a)
a%=7 #same as a=a%7
print(a)
a**=6 #same as a=a**6
print(a)
a//=7 #same as a=a//7
print(a)

#comparison operator

print(5==3)#equality check 
print(5!=3)#not equal to check
print(5>3)# greater than check 
print(5<3)#less than check
print(5<=3)#less than equality check
print(5>=3) #greater than equal check

#logical operater

x=3
print(x<5 and x<8)#returns true only if both the condition satisfies
print(x>1 or x>5)#returns true if atleast one of them is true 
print(not(x<5 or x>1))#returns vice versa of or operator
print(not(x<5 and x>2))#returns vice versa of and operator
 
# identity operators

a = [10,40]
b = [10, 40]
c=a
print(c is a)# a and c are in same adress so returns 
print(b is c) #although the values are same its not same object
print( a == b ) # retuns true as both have same value
 #is not operater returns true only when both the object are not in same memory location
print(a is not c)
print(a is not b) 
print(a!=b)

#membership operator
# these operator are used to check if some sequence is present

s = [10,20,30,40,50]
print(30 in s)
print(50 not in s)
# not in operator returns true only when element is not present in sequence

#bitwise operator

# they are used to compare binary operator
# & => AND => if both bits are 1, it sets each bit to 1 , otherwise 0

# | => OR => if one of the two bits is 1 , it sets each bit to 1 , otherwise 0

# ^ => XOR => if only one of the two bits is 1 , it sets each bit to 1

# ~ => NOT => complement operator, it returns one's complement of the number

# << => Zero fill left shift => the binary number is appended with 0's at the end

# >> => Right SHift => In simple terms, the right side of the bits are removed

a = 60
b = 13
print(a&b)
print(a|b)
print(a^b)
print(~a)





