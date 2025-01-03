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