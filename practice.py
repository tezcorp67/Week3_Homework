# Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry about strings with less than two characters.

# define a function
# input: string
# output: copy that removes first and last char of input string

def removeFirstAndLast(myString):

    result = myString[1:-1]

#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#For example (Input -> Output):
#summation(2) -> 3 (1 + 2)
#summation(8) -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
    
def grasshopper_sum(num):
    total = 0
    for int in range(num+1):
        total += int
    return total

print(grasshopper_sum(8))