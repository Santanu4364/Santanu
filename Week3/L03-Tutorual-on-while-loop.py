#let us find the number of digits in a number
num=abs(int(input("Enter a number: ")))
digits=1
while(num>9):
    num=num//10
    digits=digits+1
print("the number of digits in the number is: ", digits) 

#let us find the reverse of a number
num=abs(int(input("Enter a number: ")))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("the reverse of the number is: ", rev)
