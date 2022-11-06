#.format(value1 ,value2,value3.....)
#it formats the specific value and put them inside the placeholder
#placeholder=>{}
text = "my name is {}, i am {} years old".format("john",20)
print(text)
#formatting types
#inside the placeholder you can write different formatting types to format the result
#some of them are mentioned below
# :<
# :>
# :F
# :f

#.:f fix point number format 
text = "The price of this product is {:.f} rupees"
text = "The price of this product is {:.4f} rupees"
text = "The price of this product is {:.2f} rupees"
print(text.format(25))

numbers = [22,50,40,30,40.25,9.13567]
for x in numbers:
    print("{:.3f}".format(x))

#:.%
text='i scored {:.0%} percentage in the test'
print(text.format(0.25))


