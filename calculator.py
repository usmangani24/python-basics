def add(a, b):
    return a + b

def add(a, b):
    return  a - b

def add(a, b):
    return a * b 

def add(a, b):
    return a / b

print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = int(input("Choice likho (1-4): "))
x = int(input("First number: "))
y = int(input("Second number: "))

if choice == 1:
    print("Ressult:", add(x, y))

elif choice == 2:
    print("Result:", sub(x, y))

elif choice == 3:
    print("Result:", mul(x, y))

elif choice == 4:
    print("Result:", div(x, y))

else:
    print("Wrong choice  ❌")