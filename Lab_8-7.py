# Author: PCL 12/7/22

#creating a function which checks if the inputted word is a palindrome and outputs true or false
def is_palindrome(word):
    #preventing capitalization from giving false negatives by lowercasing everything
    lowered_word = word.lower()
    #creating a empy list where the inputted string will be broken into a list of individual chracters and eventually reversed
    palindrome_list = []
    #defining a count which will go over each character of the list
    count = 0
    while (count < len(lowered_word)):
        palindrome_list.append(lowered_word[count])
        count += 1
    #reversing the first list
    palindrome_list.reverse()
    #turning the reversed list back into a string
    palindrome = "".join(palindrome_list)
    #returning the results of checking the reversed lowered word against the original
    return (palindrome == lowered_word)

#getting an input from the user
x = input("Please input the word that you would like to have checked for if it is or is not a palindrome: ")

#printing the check
print(is_palindrome(x))

#I wish I didnt need to use a loop for this
def better_is_palindrome(word):
    palindrome = "".join(word[::-1])
    return (palindrome.lower() == word.lower())

#printing the much shorter functions check
print(better_is_palindrome(x))