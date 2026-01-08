alpha="abcdefghijklmnopqrstuvwxyz"
i=0
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])
# if i write alpha[i+26] it will give error as index out of range
# there is a way to solve this problem using modulus operator
print("using modulus operator")
i=25
print(alpha[(i+1)%26])  # Output: a
print(alpha[(i+2)%26])  # Output: b
print(alpha[(i+3)%26])  # Output: c
#so using modulus operator we can wrap around the index
print("example problem")
s="india"
#i expext to output "joejb"
#so each letter is shifted by 1 position
i=0  #index of the letter in string "india"
k=1   #number of positions to shift
print(alpha.index(s[i]))  # Output: 8
t=''
t=t+(alpha[(alpha.index(s[i])+k)%26])
t=t+(alpha[(alpha.index(s[i+1])+k)%26])
t=t+(alpha[(alpha.index(s[i+2])+k)%26])
t=t+(alpha[(alpha.index(s[i+3])+k)%26])
t=t+(alpha[(alpha.index(s[i+4])+k)%26])
print(t)  # Output: joejb
  # Output: 9
#here k is the number of positions to shift
