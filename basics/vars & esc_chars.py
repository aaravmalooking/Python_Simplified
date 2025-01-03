# welcome to vars (variables) and esc_chars (escape characters)
# so, what are variables?
# variables are containers that store values.
# for example, let's say you have a variable called name, and you want to store your name inside it.
# so, you can do this:
name = "Aarav"
print(name)
# here the name stores the string value Aarav, which basically means in simple language that you have a box that stores the value Aarav.
# we are not done with variables, you will sometimes be using it to store value and to take input and more things.
# let's look at data types...
'''
Data types:
    1. String --> (str) stores values like "Hello", these are the values that are written inside double quotes, storing only letters, they can store numbers but we have int and float for that.
    2. Integer --> (int) stores values like 1, 2, 3, it is used for numbers which DO NOT have decimals. (You need to use this instead of str to store numbers because then the Python interpreter will treat the number stored in str value as a string.)
    3. Float --> (float) stores values like 1.1, 2.2, 3.3, it is used for numbers which DO have decimals. (You need to use this instead of str to store numbers because then the Python interpreter will treat the number stored in str value as a string.)
    4. Boolean --> (bool) stores values True or False. it is required many times by if statements and when you want to know when something is correct or wrong.
    5. List --> A data collection (Which you will learn later)
    6. Tuple --> A Data collection (which you will learn later)
    7. Dictionary --> A data collection which stores key and value (which you will learn later)
    8. Set --> A Data collection (which you will learn later)
    9. None --> (NoneType) sometimes you need variables to store no value and also store a value at the same time, that is when the None comes in.
'''

# now let's look at escape characters;
# these are characters that are used to escape other characters.
# for example, let's say you want to print a double quote inside a string.
# you can do this:
print("Hello, \"Aarav\"")
# this will print Hello, "Aarav"
# now let's look at some more escape characters:
# \n --> new line
# \t --> tab
# \r --> carriage return
# \f --> form feed
# \v --> vertical tab
# \ooo --> octal value
# \xhh --> hex value

# you can also declare variables in one line multiple variables.
a, b, h = 3,7,8
# dealers a, b, h, with values 3, 7, 8 respectively,
# you can even declare variables with the same value.
u=o=q=1
# declares u, o, q, with value 1
# if you want to declare a variable first and then assign the value later, you can do that like this.
# here our none type comes in.
x = None
# now we will declare x on the next line.
x = 63
# seems good, right?

# inputs:
# you see till now you were just declaring things by yourself and not asking anything to the user,
# but this would not be the case in real production environments.
# that's where the input function comes in, it is used to take input from the user who is running the program.
# input function takes the input from a user and stores it as a value of a variable.
username = input("Enter Your Name --> ") # always add a space here
print("Hello ", username)
# as then the user typing will be stick to the last word of the prompt
# (prompt is when you tell the user what they should type in the input field)


# also sometimes you would want to tell the interpreter that to treat the variable to store as an int.
# casting can do this.
age = int(input("Enter Your Age --> "))
# now just like any other variable, you can print its value
print(age)

# practice time!
# navigate to practice/vars & esc_chars (prac.).py and follow the tutorial from there onwards.




