# strings in python are surrounded in '' or ""
name = 'Aarav' # is same as name = "Aarav"
# you can print quotes inside quotes as long as the inside quotes don't match the outside quotes.
print("My name is also known as 'Aarav Maloo'")
# you can also assign multi-line strings to a variable

multi_line_string = """My name is also known as 'Aarav Maloo'
I am a student of BCA 3rd year""" # just note I am not a student of BCA 3rd year

print(multi_line_string)

print("Hello, World")
# even these are strings
# hello world is a string but not assigned to a variable
# strings in python are arrays of bytes representing Unicode chars.
# so like other languages, you can even get chars from any string.


print(name[1]) # INDEXES ALWAYS START WITH 0
# so name[0] is A, name[1] is a, name[2] is r, name[3] is a, name[4] is v

# if you want to know if some string is in a variable in keyword.
taxes = "Raising taxes upto 20%"
print("taxes" in taxes)

# if you want to get the length of a string
print(len(taxes))

# not in is also there, which is the opposite of in

print("lowering" not in taxes)
# there is also many other functions in strings you can use.

# there is slicing, which is used to get parts of a string.
# so using that logic, you can index like this:

print(name[2:]) # skip aa and get rav
print(name[2:4]) # will print ra

# if you want to get the parts from behind, use negative indexing...
# negative indexing is when you want to get the last of the string.

print(name[-5:-1])
