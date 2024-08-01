num1 = 10
num2 = 5

num1 += num2
print(num1)
num1 -= 1
print(num1)
num1 *= num2
print(num1)
num1 -= 60
print(num1)
num1 **= 2
print(num1)


# integer division
num1 //= 2
print(num1)

# float division - A float cannot be converted into int without typecasting even if you use // it will still result in float
num1 /= 2
print(num1)

# tried int division
num1 //= num2
print(num1) # result 5.0


num1 %= 1
print(num1) # result 0.0 - Remember the float will stay float