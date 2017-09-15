# -*- coding: utf-8 -*-
# PROJECT EULER
# Problem 6
# Problem Statement: The sum of the squares of the first ten natural numbers
# is, 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
# ANSWER: 25164150

sum_of_squares = 0
square_of_sums = 0

for i in range(1, 101):
    sum_of_squares += (i * i)
    square_of_sums += i

square_of_sums *= square_of_sums

print('The difference between the square of the sums (' + str(square_of_sums) +
      ') of the first 100 natural numbers and the sum of the squares (' +
      str(sum_of_squares) + ') of the same numbers is: ' +
      str(square_of_sums - sum_of_squares) + '.')
