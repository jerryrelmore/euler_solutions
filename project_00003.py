# PROJECT EULER
# from https://projecteuler.net/
# Problem 3 solution
# Problem statement: The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# ANSWER: 6857

import itertools

limit = 600851475143

for i in itertools.count(1):
    if limit % i == 0:
        limit /= i
        print("Size of limit: ", limit)
        print("Factor: ", i)
    if limit == 1:      # wes hould evenutally reach that point where limit is reduced to 1
        break

    
    
