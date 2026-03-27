#let us find the factorial of a number
print("enter a number: ")
n=int(input())

#n=5
#n!=1*2*3*4*5
'''ans=1
ans=ans*1
ans=ans*2
ans=ans*3
ans=ans*4
ans=ans*5
print(ans)'''

i=1
ans=1
while(i<=n):
    ans=ans*i
    i=i+1
print(ans)