# 1. Write a python program to add two numbers.
# 2. Write a python program to find remainder when a number is divided by z.
# 3. Check the type of variable assigned using input() function.

# 4. Use comparison operator to find out whether ‘aʼ given variable is greater than ‘bʼ or not.
# Take a = 34 and b = 80

# 5. Write a python program to find an average of two numbers entered by the user.
# 6. Write a python program to calculate the square of a number entered by the user.

# problem 1
a = 5 
b = 10
sum = a + b
print("The sum of a and b is", sum)

# problem 2
num = 10
z = 3
remainder = num % z
print("The remainder when", num, "is divided by", z, "is", remainder)

# problem 3
c = input("Enter a value: ")
print("The type of variable c is", type(c))

# problem 4
d= 34
e = 80
is_greater = d > e
print("Is a greater than b?", is_greater)

# problem 5
f = float(input("Enter first number: "))
g = float(input("Enter second number: "))
average = (f + g) / 2
print("The average of the two numbers is", average)

# problem 6
h = float(input("Enter a number to find its square: "))
square = h ** 2 
print("The square of the number is", square)
print("The square of the number is", h * h)  # alternative way to calculate square
print("The square of the number is", pow(h, 2))  # using built-in pow function
# print( "The square of the number is", h^2)  #not valid in python 