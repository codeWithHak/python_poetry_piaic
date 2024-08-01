# if you have a solid number it's called an integer
numInt = 10

# if you have a decimal value its called float
numFloat = 10.11


# performing arithmetic operations
#num1 = 5
#num2 = 10

#addition
#print(f"{num1} + {num2} = {num1 + num2}\n")

#subtraction
#print(f"{num1} - {num2} = {num1 - num2}\n")

#division
#print(f"{num1} ÷  {num2} = {num1 / num2}\n")

#multiplication
#print(f"{num1} x {num2} = {num1 * num2}\n")

#addition
#print(f"{num1}² = {num1 ** 2}\n")


# typecasting
 

# casting into string 
#num1 = str(22)
#num2 = str(10.11)
#num3 = str(99)

#print(f"num1: {num1}, typeof num1: {type(num1)}\n")
#print(f"num2: {num2}, typeof num2: {type(num2)}\n")
#print(f"num3: {num3}, typeof num3: {type(num3)}\n")

# the following code will concatinate all the nums instead of adding them because they are strings now
#print(num1 + num2 + num3)




# casting into int
"""
num1 = int("15") # 15
num2 = int(10.11) # 10
num3 = int(False) # 0
print(f"num1: {num1}, typeof num1: {type(num1)}\n")
print(f"num2: {num2}, typeof num2: {type(num2)}\n")
print(f"num3: {num3}, typeof num3: {type(num3)}\n")

"""
# this will add all 3 and result in 25. False == 0 , True == 1
#print(num1 + num2 + num3)


# casting into float
num1 = float(15) # 15.0
num2 = float("10") # 10.0
num3 = float(False) # 0.0
print(f"num1: {num1}, typeof num1: {type(num1)}\n")
print(f"num2: {num2}, typeof num2: {type(num2)}\n")
print(f"num3: {num3}, typeof num3: {type(num3)}\n")

# this will add all 3 but result in 25.0 False == 0 , True == 1
print(num1 + num2 + num3)


# finding id of all values


num1 = float(15) # 15.0
num2 = float("10") # 10.0
num3 = float(False) # 0.0
print(f"num1: {num1}, typeof num1: {type(num1)} id: {id(num1)}\n")
print(f"num2: {num2}, typeof num2: {type(num2)} id: {id(num2)}\n")
print(f"num3: {num3}, typeof num3: {type(num3)} id: {id(num3)}\n")


