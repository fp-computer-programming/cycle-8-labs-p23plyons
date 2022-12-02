# Author: PCL 12/2/22

#creating a function for the sum of a number and all numbers before it to 0
def num_sum(num):
    #setting a variable for the sum to be totaled in
    sum = 0
    #creating a for loop to iterate over every number from 0 up to the input and add them to the sum
    for x in range(num+1):
        sum += x
    return(sum)

#creating an input for the function
x = input("Please input a number you would like to find the sum of all the numbers up to and including itself: ")

#printing results
print(num_sum(int(x)))
