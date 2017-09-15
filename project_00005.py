# PROJECT EULER
# Problem 5
# Problem Statement: 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder. What is the smallest
# positive number that is evenly divisible by all of the numbers from 1 to 20?
# ANSWER: ???

import itertools

number = 0
count = 0
step_size = 20

def step_change(old_step_size, divisor):
    x = old_step_size
    while (x % divisor != 0):
        x += 20
    return x    

print('Calculating')
for i in itertools.count(20, step_size):
    for x in range(20, 2, -1):
        if (i % x == 0):
            count += 1
        else:
            step_size = step_change(step_size, x)
            break
    if (count != 19):
        count = 0
    elif (count == 19):
        number = i
        print(number)
        break
    print(str(i) + ' and step size: ' + str(step_size))

print('The smallest positive number that is evenly divisible by all numbers from 1 to 20 is ' + str(number) + '.')
