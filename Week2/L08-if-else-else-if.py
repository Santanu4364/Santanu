# Check if a number is even or odd
print("Enter a number: ")
num=int(input())
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")


num=int(input("Enter a number: "))
if(num%5==0):
    if(num%10==0):
        print("last digit is 0")
    else:
        print("last digit is 5")
else:
    print("number is from other category")

