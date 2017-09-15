# PROJECT EULER
# from https://projecteuler.net/
# Problem 1 solution - similar to FizzBuzz
# Problem statement: If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# ANSWER: 233168

sum = 0

for i in range(1, 1000):
    alreadyCounted = False
    if (i % 3 == 0) and (i % 5 == 0):
        sum += i
        alreadyCounted = True
    elif (i % 5 == 0) and alreadyCounted == False:
        sum += i
        alreadyCounted = True
    elif (i % 3 == 0) and alreadyCounted == False:
        sum += i
        
print(sum)
