# Author: OMKAR PATHAK

# Python program to reverse the words

userInput = input("Enter the word that needs to be reversed:")
#the above function display the string and takes a string value.

userInput = userInput.split()
#.split() is an inbuild function that splits the given word to sub-letters.

print(' '.join(userInput[::-1]))
# the above line take the user defined function namely userInput and print the index from the last character to the first character 
# the join function in the 11th line is used to join the reversed word with suceeding word with a space.

# OUTPUT:
# Computer Science
# Science Computer
