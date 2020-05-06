'''
Write a program to determine if a number, given on the command line, is prime.

1. How can you optimize this program?
2. Implement[The Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
of the oldest algorithms known(ca. 200 BC).
'''
# --------------------#UPER#--------------------#
# --------------------
# Understand: Have the person enter a number(input), display if the numer is a prime or not(output)
# --------------------
# Plan:
# create input
# if - else to rule out "prime" if number is < 1
# if number is > 1, check for factors
# check for factors with is: x % y == 0
# if number has no factors print "is not a prime"
# if number has factors, print out factors
# --------------------
# Execute:

num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # iterate through and list out why it's not prime
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)  # 2 x 5 = 10, 5 x 2 = 10
        else: 
            print("Number is prime")  #NOTE: IDK why but it prints this no matter what instead of only if the number is prime

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "Enter a number greater than 1 to check if it is prime.")
