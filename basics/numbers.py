# welcome to numbers.py
'''
Data types for numbers:
Complex --> used for complex numbers
int --> Used for numbers which DO NOT have decimals.
Float --> used for numbers which HAVE decimals.
'''

mycomplex = 12.4j
myint = (int(12))
myfloat = (float(12.567))

# you can get the types of the variables using the type() function...

print(type(mycomplex)) # outputs <class 'complex'>
print(type(myint)) # outputs <class 'int'>
print(type(myfloat))# outputs <class 'float'>


# you can almost perform arithmetic calculations with numbers.

print(12 + 12) # outputs 24
print(12 - 12) # outputs 0
print(12 * 12) # outputs 144 # * is used for multiplication
print(12 / 12) # outputs 1.0 # / is used for division
print(12 % 12) # outputs 0 # % is used for modulus, which returns the remainder of a division.
print(12 ** 12) # outputs 1048576 # ** is used for exponentiation


# this will be helpful creating a calculator in python, also in machine learning and artificial intelligence.
# numpy, a module for scientific computing which would again require numbers.
# numpy_simplified will be also coming soon.
