'''
Name:           Francisco McGee
Assignment:     DigitsProduct Assignment from Code Fights
Github:         

Question Text:
Given an integer product, find the smallest positive (i.e. greater than 0) 
integer the product of whose digits is equal to product. If there is no such 
integer, return -1 instead.

Test Cases (as dictionary):
key = input number, value = expected output
test = {12 : 26,
    19 : -1,
    450 : 2559,
    0 : 10,
    13 : -1,
    1 : 1,
    243 : 399,
    576 : 889,
    360 : 589,
}

Challenges: 
This problem was very straightforward for me when I imagined my method, the 
"factor sieve." One thing I would love to try is to smoosh the code together 
using list comprehensions. List comprehensions are a skill I am eager to learn.

General Strategy:
(1) handle edge cases: 0, 1, then anything less than 10, because they're 
    annoyingbut reasonable for hand-wavy math reasons
(2) "factor sieve" method
    - create a list of single digit factors from 9 -> 2
    - use this list as "factor sieve," where the first hole in the sieve is the 
    largest possible single digit factor
    - the idea is that if you create the result using the sieve in this "biggest 
    factor first" way, then you will minimize the left-most place of the result, 
    which will result in the lowest positive integer    
(3) while product != 1 loop
    - in this loop, the idea is that we need to loop through the product and use 
    the factor sieve each time until we reach the stop condition
    - if the factor "falls through" the sieve and into the product, then a 
    number of things need to happen:
    1) divide the product by the factor, update the product
    2) add the factor to the beginning of the "keepers" string
    3) break out of the for loop to reset the sieve
        - by resetting the sieve in this way, we can get again try to get the 
        biggest factors to "fall through" to the right-most side of the result, 
        and the smallest factors will "fall through" on the left
    4) by continually dividing product by its factors, you will eventually get 
    product == 1; at this point, jump out of the while loop
(4) if not keepers
    - if you try to use the sieve, and nothing falls through, then keepers is 
    empty
    - this would mean that product had no single digit factors between 2 and 9, 
    so return -1
'''

def digitsProduct(product): 
# (1)
    if product == 0:
        return 10
    elif product < 10:
        return product

# (2)
    factors = range(9, 1, -1)
    keepers = ""

# (3)
    while product != 1:
        for factor in factors:
            if product % factor == 0:
                product /= factor
                keepers = str(factor) + keepers
                break
# (4)
        if not keepers:
            return -1    
            
    return keepers
 
# test = [12, 19, 450, 0, 13, 1, 243, 576, 360]   
test = {12 : 26,
    19 : -1,
    450 : 2559,
    0 : 10,
    13 : -1,
    1 : 1,
    243 : 399,
    576 : 889,
    360 : 589,
}

for key, value in test.items(): 
    print "testing: ", key, "  should be: ", value, "  actual: ", digitsProduct(key)