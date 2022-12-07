# Author: PCL 12/7/22

#creating a function to count how many letter "a"'s are in a string
def count_a(word):
    #lowercasing whatever string is input
    lowered_word = word.lower()
    #turning the inputted string into a list of individual characters
    lowered_word[::-1]
    #defining a count for the while loop and the number of a's detected
    count = 0
    num_a = 0
    while (count < len(lowered_word)):
        if (lowered_word[count] == "a"):
            num_a += 1
        count += 1
    return (num_a)

#getting an input from the user
x = input("Please input any word that you would like to know the number of letter a's it contains: ")
#printing the number of a's detected by the function
print(count_a(x))