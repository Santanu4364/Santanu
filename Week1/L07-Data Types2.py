i=10
f=5.6
s='india'
#Incase of boolean we have two values only True or False 
#and the first letter should be in capital
b1=True
b2=False

print(type(1))
print(type(f))
print(type(s))
print(type(b1))
print(type(b2))
#how to convert one data type to another data type
a=int(5.6)
b=int('10')
print(a,type(a))
print(b,type(b))

a = bool(10)
b = bool(0)
c = bool(-5)

print(a,type(a))
print(b,type(b))
print(c,type(c))

#in this case the 0 only value which is converted to False
#all other values are converted to True

#convert string to boolean
a = bool('india')
b = bool('10')
c = bool('10.2')
d= bool('0')
c=bool('')

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(c,type(c))
#in this case all the strings are converted to True
#even '0' is converted to True because it is a non empty string
#only empty string is converted to False

