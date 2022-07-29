age = input("What is your current age:")

years_to_death = 90 - int(age)
days = years_to_death * 365
weeks = years_to_death * 52
months = years_to_death * 12
print("You have " + str(days) + " days, " + str(weeks) + " weeks, " + str(months) + " months left.")