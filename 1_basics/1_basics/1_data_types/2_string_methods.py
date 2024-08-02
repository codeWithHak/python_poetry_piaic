name:str = "huzair ahmed khan"
#some basic string methods
# print(name.title())
# print(name.upper())
# print(name.lower())


# f-string 

father_name = "mukhtar ahmed khan"
# print(f"Student: {name.title()}, Father: {father_name.title()}")
# print("Name: " + name.title() +'\nFather\'s name: ' + father_name.title())




# print('hello\nhi\nbye')

# print("hello\
# hi\
# bye")

# print('''hello
# hi
# bye''')


# three ways of doing the same thing
strings = "Hello my name is {} and I'm {} years old".format("Huzair",18) 
# print(strings)

strings = "Hello my name is {0} and I'm {1} years old".format("Huzair",18) 
# print(strings)

strings = "Hello my name is {name} and I'm {age} years old".format(name="Huzair",age=18) 
# print(strings)

# you can also tell how many space a placeholder should acquire
strings = "Hello my name is {name:6} and I'm {age:2} years old".format(name="Huzair",age=18) 
# print(strings)

#if you want spaces before the character
strings = "Hello my name is {name:>8} and I'm {age:2} years old".format(name="Huzair",age=18) 
print(strings)

# spaces will be equally divided from both sides
strings = "Hello my name is {name:^8} and I'm {age:2} years old".format(name="Huzair",age=18) 
print(strings)