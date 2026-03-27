#!/usr/bin/env python3
s = 'good'
print(s*5)  # Output: goodgoodgoodgoodgood
print(s[0]*5)  # Output: ggggg

# String comparison
# Equality comparison

x = 'india'
print(x == 'india')
print(x == 'India')

# Lexicographical comparison

print('apple' > 'one')
print('four' < 'ten')
print('cat' < 'car')

#string indexing and slicing
s ='python'
print(s[0])    # Output: p
print(s[1])    # Output: y
print(s[-1])   # Output: n
print(s[-2])   # Output: o
#so the indexing starts from 0 from left to right and -1 from right to left
#slicing
print(s[0:3])   # Output: pyt
print(s[2:5])   # Output: tho

s = 'santanu--mandal'
print(len(s))
print(s[14]) 
