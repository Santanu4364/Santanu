#The operators are special symbols that carry out arithmetic
#or logical computation.
#examples of operators are +, -, *, /, etc.

a=8
b=4
n=a+b
print(n)

#Concatenation of two strings (put tow words together)

a='santanu'
b='mandal'
n=a+b
print(n)

#union of two lists using + operator as concatenation

a=[8,9,4]
b=[5,7,3]
n=a+b
print(n)


a=11
b=25
n=a/b
print(n)

n=10+13*2
#my guess is 46
#so the expected answer is incorrect, the actual answer is 36
#due to operator precedence
print(n)
#it is 36 because * has higher precedence than +

t=(10+13)*2
print(t)
#now the answer is 46