# Author: PCL 12/2/22

#creating a function to take a list of names and print multiple invites with each name
def name_list(names):
    for x in names:
        print("Hi "+x+", you're invited to my party on Friday!")

#creating an input for wether or not the user would like to invite another person
x = input("Would you like to input another name? Y/N: ")
new_name = x.lower() == "y"

#empty list for the names to be compiled in
names = []

#creating a loop that promts the user for the name of who they would like to invite, adds that name to a list,
# and then checks if they would like to input another name. This is repeated until the user decides they do not want to input another name.
while (new_name == True):
    names.append(input("Please input the name of the person you would like to invite to the party: "))
    x = input("Would you like to input another name? Y/N: ")
    new_name = x.lower() == "y"

name_list(names)
