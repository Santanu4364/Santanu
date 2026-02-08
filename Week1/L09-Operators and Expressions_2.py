#operatoes are divided into 3 major categories
#1. Arithmetic Operators
#2. Comparison Operators
#3. Logical Operators

#1Arithmetic Operators(+, -, *, /, %, //, **)

print('addition:', 3 + 2)
print('sunstraction:', 3 - 2)
print('multiplication:', 3 * 2)
print('division:', 3 / 2) 

print('floor division:', 9 // 2) 
#floor division gives the integer part of the division

print('modulus:', 9 % 2)
#modulus operator gives the remainder

print('exponent:', 3 ** 2)
#exponent operator gives the power

#2. Comparison Operators (==, !=, >, <, >=, <=)
#comparison operators are used to compare two values
#the result of a comparison is either True or False

print(3 > 5)
print(10<15)
print(5 >= 5)
print(5<5)
print(5==5)
# == is used to check equality
print(5!=5)

#3. Logical Operators (and, or, not)

#and operator
#and operator returns True if both the operands are True
#otherwise it returns False
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or operator
#or operator returns True if at least one of the operands is True
#otherwise it returns False
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not operator
#not operator returns True if the operand is False
#it returns False if the operand is True
print(not (True))
print(not (False))
