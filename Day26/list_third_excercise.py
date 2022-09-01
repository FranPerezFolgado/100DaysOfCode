

with open('Day26/file1.txt') as file_one:
    one_letters = file_one.readlines()

with open('Day26/file2.txt') as file_two:
    two_letters = file_two.readlines()

result = [int(x) for x in one_letters if x in two_letters]
print(result)
