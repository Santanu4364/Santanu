n = int(input())

for _ in range(n):
    line = input()
    result = ""
    
    for ch in line:
        if ch.lower() in "aeiou":
            result += ch.upper()
        else:
            result += ch.lower()
    
    print(result)