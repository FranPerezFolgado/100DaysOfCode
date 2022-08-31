print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
friends = int(input("How many people to split the bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
each = ((bill * tip/100) + bill) / friends
print("Each one must pay " + str(round(each,2)) + "$")