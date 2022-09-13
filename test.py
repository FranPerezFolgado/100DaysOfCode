

try:
    with open("testfile.txt", mode='r') as file:
        print(file.read())

except FileNotFoundError:
    print("The file doesn't exists.")
else:
    print("The file exists!")
finally:
    print("This will always be printed.")