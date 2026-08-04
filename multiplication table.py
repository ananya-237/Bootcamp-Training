# This program prints the multiplication table of a given number
x = int(input("Enter a number:"))
print("Multiplication table of", x)
for i in range(1, 11):
    t = x * i
    print(x, "x", i, "=", t)