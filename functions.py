 #Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. 
 # For example:

def sum_to(n): 
    total = 0
    for x in n:
        total += x 
    return total 
print(sum_to((1,2,3)))


# Write a function named largest() that takes a list parameter and returns the largest element in that list. 
# You can assume the list contents are all positive numbers. 

largest = [1, 8, 11, 50, 101, 58]
largest2 = [10, 4, 2, 231, 91, 54]
print("largest number is: ", max(largest))
print("largest number is: ", max(largest2))

# Write a function named occurances() that takes two string parameters and counts the number of occurrances of 
# the second string inside the first string. For example:

occurances = ('fleep floop')   # returns 2
occur_count1 = occurances.count('e') # coutning character of e.
print("The count of 'e' is", occur_count1)


occurances = ('fleep floop')   # returns 2
occur_count2 = occurances.count('p')
print("The count of 'p' is", occur_count2)



occurances = ('fleep floop')  # returns 1
occur_count3 = occurances.count('ee')
print("The count of 'ee' is", occur_count3)



occurances = ('fleep floop')  # returns 0
occur_count4 = occurances.count("fe")
print("This count of 'fe' is",occur_count4)




# Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product.
#  (HINT: Review your notes on *args).

# how many arguments that will be passed into your function, add a * before the parameter name
#in the function def.
# the function will receive a tuple of arguments, and can access the items accordingly.

def product(*cars): 
    print("My fave car is: " + cars[2])
product("Benz","Tesla","BMW","Lexus")














