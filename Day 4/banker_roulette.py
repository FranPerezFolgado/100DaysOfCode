import random

names_str = input("Give me everybody's name, separated by a comma. ")
names = names_str.split(", ")
num_names = len(names)
pay_bill_name = random.choice(names)
#random_name = random.randint(0, len(names)-1)
#pay_bill_name = names[random_name]
print(f"{pay_bill_name} should pay the bill")