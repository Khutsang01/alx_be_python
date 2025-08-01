# Multiplication Table Generator

# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

#Generate and print the multiplication table fro 1 to 10
for Y in range(1, 11):
    product = number * Y
    print(f"{number} * {Y} = {product}")
print()
