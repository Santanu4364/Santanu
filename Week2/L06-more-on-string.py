alpha="abcdefghijklmnopqrstuvwxyz"
i=0
print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])
# if i write alpha[i+26] it will give error as index out of range
# there is a way to solve this problem using modulus operator
print("using modulus operator")
print(alpha[(i+26)%26])  # Output: a