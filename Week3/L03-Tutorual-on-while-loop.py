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


#reverse of a negative number with sign
n=int(input("number: "))
absNum=abs(n)
rev=0
while(absNum>0):
    r=absNum%10

    rev=rev*10+r
    absNum=absNum//10
if (n>0):
    print(rev)
else:
    print(rev-2*rev)

#find the number is palindrome or not
n=int(input("number: "))
absnum=abs(n)
rev=0
while(absnum>0):
    rem=absnum%10
    rev=rev*10+rem
    absnum=absnum//10
if(n<0):
    rev=rev-rev*2
if(rev==n):
    print("palindrom")
else:
    print("not a palindrom")