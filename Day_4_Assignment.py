##1) use string functions to count the occurrence of 'y' in a word given by user.

str= input("Enter your string : ")
cont=str.count("y")
print("y count into given string '{}' is {}.".format(str,cont))


##take input of a string and print it's even indexed characters

str= input("Enter your string : ")

print("Your Sting with even indexes '{}'.".format(str[ : : 2]))


##3)create a program to swap case. Using string functions
##Input : *EdUyEaR*
##Output :.  *eDuYeAr*

str= "EdUyEaR"

print("Swapcase output is '{}' .".format(str.swapcase()))
