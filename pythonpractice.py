#learning arrays
#slicing strings
set = "set of integer"
print(set[2:8])

#using negative indexe
print(set[-8:-2])

#splitting
text = set.split()
print(text)

#replacements
set = "set of integer"
print(set.replace("integer","complex number"))

#booleans:gives value in true and false
print(50>30)
print(50==30)
print(50<30)
print(bool("morning"))
print(bool(856))
print(bool())

#listing
mylist = [10,20,30,40]
#finding length of a list
print(len(mylist))

#finding type of a list
print(type(mylist))
 
 #slicing elements from list with respect to index no.
print(mylist[3])
print(mylist[-3])

#slicing elements from list with respect to range.
print(mylist[2:5])
print(mylist[-4:-1])

#inserting element to list with respect to index no.
mylist[2] = 30
print(mylist)

#replacing element with respect to its range
mylist[1:2] = [200,300]
print(mylist)

#append used to insert element in a list
mylist.append('preet')
print(mylist)

#with help of pop we can vanish the element of given index no.
mylist.pop(3)
print(mylist)

#with help of extending we combine two lists
myList1 = ['apple' ,'banana', 'cherries' , 'oranges']
myList2 = ['cashew','almonds']
myList1.extend(myList2)
print(myList1)

#deleting element from list of reqired index no.
del myList1[2]
print(myList1)

#to vanish whole list
myList1.clear()
print(myList1)

