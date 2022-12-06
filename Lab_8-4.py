# Author: PCL 12/6/22

#creating a function which prints the sum of all numbers from zero to, and including the input
def sum_to(n):
    #where the sum will be counted
    total = 0
    #counter for the while loop
    count = 0
    while (count < int(n)):
        count += 1
        total += count
    return (total)

#creating an input for the function
n = input("Please input a number you would like to find the sum of all the numbers up to and including itself: ")

#printing the results to the console
print(sum_to(n))