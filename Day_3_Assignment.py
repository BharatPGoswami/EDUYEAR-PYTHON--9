##AGE CALCULATOR 
##1)  calculate Age of a person - User should enter the year of birth and the program should output the age..
##eg : entered value is 1990, output age is 30

year=int(input("Please enter your year of birth... "))

age=2021-year

print("Entered year of birth is {}, your age is {} year.".format(year,age))



##2) Simple Calculator:
##- get 2 numbers from the user and print the result of addition, subtraction, multiplication and
##floor division, decimal division, remainder, power of the input numbers

num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second number: '))

print("a + b = {}".format(num1 + num2 ))
print("a - b = {}".format(num1  - num2 ))
print("a * b = {}".format(num1  * num2 ))
print("a / b = {}".format(num1  / num2 )) 
print("a % b = {}".format(num1  % num2 ))
print("a // b = {}".format(num1  // num2 ))
print("a ** b = {}".format(num1  ** num2 ))
