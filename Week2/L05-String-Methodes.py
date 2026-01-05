x="my Self is SANTanu"
print(x.lower())  # Output: my self is santanu
print(x.upper())  # Output: MY SELF IS SANTANU
print(x.capitalize())  # Output: My self is santanu
print(x.title())  # Output: My Self Is Santanu
print(x.swapcase())  # Output: MY sELF IS santANU
x="santanu"
print(x.islower())
print(x.isupper())
print(x.istitle())
x="123"
y="123abc"
print(x.isdigit())
print(y.isdigit())
print("**********isalpha")
z="abc"
print(z.isalpha())
print(y.isalpha())
print(y.isalnum())
print("************strip")
x=("*********santanu*******")
print(x.strip('*'))
print(x.lstrip('*'))
print(x.rstrip('*'))

x="python"
print(x.startswith('P'))
print(x.startswith('p'))
print(x.endswith('n'))
print(x.endswith('N'))   
x="Santanu Mandal"
print(x.replace("Mandal","Das"))

print("****** startswith")
x="hello world"
print(x.startswith('h'))  # Output: True
print(x.startswith('H'))  # Output: False

print("****endswith")
print(x.endswith('d'))  # Output: True
print(x.endswith("D"))  # Output: False

print("*********Count")
x="santanu mandal is a good student"
print(x.count('a'))  # Output: 4
print("****index")
print(x.index('m'))  # Output: 8
print("*Replace")
print(x.replace('santanu','SANTANU'))
