# make a second cahnce using if else loop
print("when india got independance?: ")
year=int(input())
if year==1947:
    print("Hip Hip Hurrey. You get it!")
else:
    print("cammon you dont know this")
    print("it's okey lets try again")
    print('what is the independance year of india?: ')
    year=int(input())
    if year==1947:
        print("you get it")
    else:
        print("you are wrong again...")

# lets write a code that allow as many attempt as the user want.
# The code wil end when it will get the corrwct answer.
print("when did india get independance: ")
year=int(input())

while(year!=1947):
      print("you get it wrong")
      year=int(input())
print("Wowwwwwww you get it right")