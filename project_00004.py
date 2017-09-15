# -*- coding: cp1252 -*-
# PROJECT EULER
# from https://projecteuler.net/
# Problem 4 solution
# Problem statement: A palindromic number reads the same both ways. The
# largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# ANSWER: 906609 is the palindrome - factors are 913 and 993.

lower_limit = 10000           # 100 * 100 = 10000 so lowest palindrome must >
upper_limit = 998001          # 999 * 999 = 998001 so highest palindrom must be <
palind = 0                    # variable to store palindromes we find
num1 = num2 = 0               # variables to store 3-digit factors
palindrome = factor1 = factor2 = 0    # variables to store highest palindrome (palindrome) we find that is product of two 3-digit integers (factor1 and factor2)     

# product() function tests to see if a palindrome is the product of two 3-digit integers
def product(test_case):
    numA = 0                  # declare variables for testing integer length and divisibility
    numB = 0
    for x in range(100, 999): # we know we're only interested in 3-digit integers...
        if (test_case % x == 0) and (len(str(test_case / x)) == 3): #... that when divided by another 3-digit integer leave no remainder
            numA = x          # so the first 3-digit integer is x
            numB = test_case / x    # while the second is the palindrome divided by x
    return test_case, numA, numB    # return the palindrome, first 3-digit integer, second 3-digit integer

for i in range(lower_limit, upper_limit):   # we already know the range of possible numbers between 100*100 and 999*999
    length = len(str(i)) - 1                # let's determine the # of digits in the integer
    stringNumber = str(i)                   # convert the integer we're going to check for "palindromic" properties to a string to make it easier to check
    if (length + 1 == 5):                   # check for "palindromicity" on 5 digit integers
        if (stringNumber[0] == stringNumber[length]):   # do the first and fifth characters match?
            if (stringNumber[1] == stringNumber[length - 1]):   # do the second and fourth characters match?
                palind, num1, num2 = product(i)         # if so, call the product() function to see if the palindrome is the product of two 3-digit integers
                if (num1 > 0) and (num2 > 0):           # if the product function returns two 3-digit integers, assign them to separate variables so they're not lost
                    palindrome = palind                 # also assign returned palindrome to a separate variable so it's not lost
                    factor1 = num1
                    factor2 = num2
    elif (length + 1 == 6):                 # check for "palindromicity" on 6 digit integers
        if (stringNumber[0] == stringNumber[length]):
            if (stringNumber[1] == stringNumber[length - 1]):
                if (stringNumber[2] == stringNumber[length - 2]):
                    palind, num1, num2 = product(i)         # if so, call the product() function to see if the palindrome is the product of two 3-digit integers
                    if (num1 > 0) and (num2 > 0):           # if the product function returns two 3-digit integers, assign them to separate variables so they're not lost
                        palindrome = palind                 # also assign returned palindrome to a separate variable so it's not lost
                        factor1 = num1
                        factor2 = num2

#-----------PRINT RESULTS
print(str(palindrome) + ' is the largest palindrome from the product of two 3-digit integers.')         
print('The integers are ' + str(factor1) + ' and ' + str(factor2) + '.')
