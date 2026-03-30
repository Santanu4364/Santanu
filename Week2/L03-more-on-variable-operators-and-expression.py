# Swapping values of two variables without using a temporary variable
print("swapping variables")
X, Y = 5, 10
print(X, Y)  # Output: 5 10
X, Y = Y, X
print(X, Y)  # Output: 10 5


# Deleting a variable
print("deleting variable")
x = 10
print(x)  # Output: 10
del x
#print(x)
#print(x)  # This will raise a NameError since x has been deleted

# Incrementing a variable's value
print("incrementing without shorthand")
count = 0
count= count + 1
count = count + 1
count = count + 1
count = count + 1
print(count)  # Output: 4

# Using shorthand operator for incrementing
print("incrementing")
count = 0
count += 1 
count += 1
count += 1
count += 1
print(count)  # Output: 4

#using shorthand operator for decrementing
print("decrementing")
count = 5
count -= 1
count -= 1
print(count)  # Output: 3

# Using shorthand operator for 
print("multiplication")
count = 5
count *= 2
count *= 2
print(count)  # Output: 20


#using of in operator
print("use of in operator")

print('alpha' in 'A variable namr can only contain alpha-numeric charachters and underscores')
print('alpha' in 'A variable name must start with a letter or the underscore character')

# the output of an in operator is a boolean value
# in this case 1st statement will return True and 2nd will return False

# Using of chaining comparisons operators
print("using chaining operators")

x = 5
print(1 < x < 10)  # Output: True
print(10 < x < 20)  # Output: False
print(x < 10 < x*10 < 100)  # Output: True
print(10 > x <= 9) # Output: True
print(5 == x > 4) # Output: True