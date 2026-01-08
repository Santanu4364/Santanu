#if condition
#let us consider the movie "Avengers". this is a 13+ movie.
print("enter your date of birth: ")
birth_year=int(input())

current_year=2026

age=current_year - birth_year
if age<13:
    print("you are not allowed to watch the movie")
else:
    print("you are allowed to watch the movie")