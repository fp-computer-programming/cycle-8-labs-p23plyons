# Author: PCL 12/7/22

#creating a function which finds the factorial of any number inputted by the user
def factorial(num):
    #defining a count for the while loop so that it goes over each number and multiplies them
    count = 0
    #setting a product where all the numbers will be multiplied and saved to
    product = 1
    while (count < num):
        count += 1
        product *= count
    return(product)

#getting an input from the user
x = input("Please input the number which you would like to find the factorial of: ")

#printing the factorial of the input
print(factorial(x))