"""
PYTHON CODE - Episode 2
SERIES - Coding Ka Toofan
TEACHER - Lalit Kumar

NOTE: Please don't copy this, it will not help you understand the concepts.. try on your own.. just use it for reference if you get stuck at some point of time.
"""



# print("Hello, World!")
# print("0____")
# print(" ||||")

#COMMENTS

# - Single Line Comment

#This was my first program
# 2nd line
# 3rd line

#Multi-Line Comment

"""
Yeh mera multiline comment hai
This is my multiline comment
"""

#GKG - Gajab ka Gyaan

'This is a string'

"""
This is a multiline string
"""

# VARIABLES
# person = 'mother'

# print("This person is my " +  person + " and she is wonderful!")
# print("This person is my" ,  person , "and she is wonderful!")
#
# person = "father"
# print("This person is my " +  person + " and she is wonderful!")
# print("This person is my" ,  person , "and she is wonderful!")

# myAge = 50

#RULES for NAMING a Variable

"""
1. _myVariable or myVariable 
2. Variable name must not stat with a number
3. 

var_1 or var___3  - Correct
var-1 or var@3 - incorrect

4. myVar is not equal to MyVar

---------------------

#These are the correct ways of writing variables.
somename   = "anyname"
some_name  = "anyname"
_some_name = "anyname"
someName   = "anyname"
SOMENAME   = "anyname"
somename2  = "anyname"

# These are the incorrect ways of writing variables.
some name = "anyname"
1somename = "anyname"
some+Name = "anyname"
some-Name = "anyname"

"""

# INPUT()



# person = input("Enter your name: ")
# print("My Name is " +  person + " and I am wonderful!")

#GKG2 - Input Function always converts the user input into a string

# person = input("Enter your name: ")
# a = type(person)
# print(a)

#------------------------------#

# EXCERCISE 1

# Q1

# inputNumber = input("Enter a Number: ")
#
# print("This is the table of " + inputNumber)
#
# print(inputNumber + "x1 = " , int(inputNumber) * 1)
# print(int(inputNumber) * 2)
# print(int(inputNumber) * 3)
# print(int(inputNumber) * 4)
# print(int(inputNumber) * 5)
# print(int(inputNumber) * 6)
# print(int(inputNumber) * 7)
# print(int(inputNumber) * 8)
# print(int(inputNumber) * 9)
# print(int(inputNumber) * 10)

#Q2

# pi = 3.14
# circumference = 2 pi r

# Solution
"""
radius = int(input("Enter the Radius of Circle: "))
pi = 3.14
print("Circumference of Circle =", 2 * pi * radius)
"""

#Ques - 3

# print("*\n**\n***\n****\n*****")

#Ques - 4

# number_of_years = int(input("Please Provide the Number of years: "))

"""

1min = 60secs
1hr = 60mins
1day = 24 hrs
1 month = 30 days
1 yr = 12*30*24*60*60 secs

number of years = number_of_years * 1yr secs

"""
# total_seconds = number_of_years * 12*30*24*60*60
#
# print("Number of Seconds in ",number_of_years, "Years is", total_seconds, "Seconds")

# Question - 5

# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")

##Lalit Kumar -> Kumar Lalit

# print(last_name , first_name)

# Question 6

"""
hint
1
2
3

total = 1 + 2 + 3
avg = (1 + 2 + 3) / 3
"""

# SOLUTION

# num1 = int(input("Enter the 1st Number: "))
# num2 = int(input("Enter the 2nd Number: "))
# num3 = int(input("Enter the 3rd Number: "))
#
# total = num1 + num2 + num3
# avg = (num1 + num2 + num3)/3
#
# print("The Total of your numbers  = ", total)
# print("The average of your numbers  = ", avg)

#QUESTION - 7

# print("text", 1, 4, "AurText", sep = " ")
# Comma ke pehle aur comma ke baad kya aana hai.. that is sep = "", default value of sep = " " .. a space

# print("*","**","***", sep="\n")

"""
Hint

input: 7
output: 7---14---21---28---35
"""

# Solution

# x = int(input("Please Enter a Number: "))
# print(x, 2*x, 3*x, 4*x, 5*x, sep="---")

#QUESTION 8

"""
Hint

input - 1. Total Price of Food
        2. %age tip 
        
output -1. Tip Amount 
        2. Total Bill
"""

# price_of_food = int(input("Enter the Price of the meal: "))
# percent_tip = int(input("Enter the %age tip you want to give: "))

"""
200rs -> 

10/100 * 200 - 20
"""
# tip_amount = price_of_food * (percent_tip/100)
# total_bill = tip_amount + price_of_food
#
# print("The Total amount of tip =", tip_amount)
# print("The Total amount to be paid =", total_bill)

# CHOCOLATE PROBLEM 1
"""
2 variables, a = 2 and b = 3

1. using 3rd variable
2. without using 3rd variable
"""

# a = 2

# b = 3

# print(a)
# print(b)

# # SOME CODE

# print("After Swapping")
# print(a)
# print(b)

## HINT (ii) - using multiple variable assignment technique

# SOLUTION - Discord [https://discord.com/invite/VQ5CxzTAqf  ] > Python Solutions
