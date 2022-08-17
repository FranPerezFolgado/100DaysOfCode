import lib
import art
print(art.logo)
operations = ["+", "-", "*", "/"]
calculate = True
result = 0
while calculate:
    first = float(input("What's the first number: "))
    keep_first = True
    while keep_first:
        print('\n'.join(operations))
        operation = input("Pick an operation: ")
        second = float(input("What's the next number: "))
        result = lib.calculate(first,second,operation)
        print(f"{first} {operation} {second} = {result}")

        keep = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'exit' to end the calculator: ").lower()
        if keep == 'n':
            keep_first = False
        elif keep == 'exit':
            keep_first = False
            calculate = False
        else:
            first = result