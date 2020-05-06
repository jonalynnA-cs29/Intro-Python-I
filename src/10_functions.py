# Write a function is_even that will return true if the passed-in number is even.


def even_number(n) -> bool:
    if n % 2 == 0:
        return True


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def print_results(num):
    if even_number(num):
        print("Even!")
    else:
        print("Odd")


print_results(num)
