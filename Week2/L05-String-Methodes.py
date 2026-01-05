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
x="python"
print(x.startswith('P'))
print(x.startswith('p'))
print(x.endswith('n'))
print(x.endswith('N'))   
x="Santanu Mandal"
print(x.replace("Mandal","Das"))