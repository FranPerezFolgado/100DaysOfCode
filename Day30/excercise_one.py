fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("The index is more than the fruit list size")
    else:
        print(fruit + " pie")

make_pie(4)
make_pie(2)


