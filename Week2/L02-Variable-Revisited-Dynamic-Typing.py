#we are trying to illustrate dynamic typing in Python
a=10
print(type(a))  # Output: <class 'int'>

a=10
print(type(a))  # Output: <class 'int'>

a="hello"
print(type(a))  # Output: <class 'str'>

a = 10  # assign a numeric value before division
a = a / 2
print(type(a))  # Output: <class 'float'>
#when we divide two integers, the result is a float in Python 3
