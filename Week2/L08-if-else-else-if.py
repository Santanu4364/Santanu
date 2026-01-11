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
if marks>=90:
    print("Grade A")
if marks>=80 and marks<90:
    print("Grade B")
if marks>=70 and marks<80:
    print("Grade C")
if marks >=60 and marks<70:
    print("Grade D")
else:
    print("Grade E")

#check grade based on marks using else if
marks=int(input('enter your marks: '))
if (marks>=0 and marks<=100):
    if marks>=90:
        print("Grade A")
    elif marks>=80:
        print("Grade B")
    elif marks>=70:
        print("Grade C")
    elif marks>=60:
        print("Grade D")
    else:
        print("Grade E")
else:
    print("Invalid input")

#Convert the given flowchart into a Python code

print('travel from city A to city B')

time = int(input('enter time: '))
longer = int(input('define longer: '))

if time >= longer:
    price = int(input('Enter Price: '))
    higher = int(input('define higher: '))
    
    if price >= higher:
        print('train')
    else:
        print('coach')
else:
    price = int(input('enter price: '))
    higher = int(input('define higher: '))
    
    if price >= higher:
        print('Daytime flight')
    else:
        print('Red eye flight')

print('Arrive city B')
