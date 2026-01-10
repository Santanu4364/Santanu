# Check if a number is even or odd
print("Enter a number: ")
num=int(input())
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

# check the last digit of a number
num=int(input("Enter a number: "))
if(num%5==0):
    if(num%10==0):
        print("last digit is 0")
    else:
        print("last digit is 5")
else:
    print("number is from other category")

#check grade based on marks
marks=int(input("Enter your marks: "))
if (marks>=90):
    print("Grade A")
if (marks>=80 and marks<90):
    print("Grade B")
if (marks>=70 and marks<80):
    print("Grade C")
if (marks>=60 and marks<70):
    print("Grade D")
if (marks<60):
    print("E")
else:
    print("invalid input")
