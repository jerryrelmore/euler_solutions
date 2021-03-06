# PROJECT EULER
# from https://projecteuler.net/
# Problem 2 solution
# Problem statement: Each new term in the Fibonacci sequence is generated by
# adding the previous two terms. By starting with 1 and 2, the first 10 terms
# will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
# ANSWER: 4613732

# Using recursion to get the number

def fiboSeq(term1, term2, totalSum):
    tempVar = term2         # store the CURRENT value of term2 (for later assignment to term1)
    term2 += term1          # add term2 to itself and term1 for the next number in the Fibonacci Sequence
    term1 = tempVar         # set term1 equaul to the OLD value of term2
    if term1 % 2 == 0:      # if term1 is evenly divisible by 2...
        totalSum += term1   # add term1 to the running total sum
    print(term1)         # for debug
    if term2 > 4000000:     # if term2 exceeds 4M (since we know term2 will always exceed term1)
        print totalSum      # print the running total sum
        return              # leave the recursive function
    fiboSeq(term1, term2, totalSum)    # recursively call the present function

fibonacci = fiboSeq(1, 2, 0)     # let's get the party started

