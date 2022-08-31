def greet():
    print("hello")
    print("hello1")
    print("hello2")


greet()


def greet_with_name(name):
    print(f"hello {name}")
    print("hello1")
    print("hello2")

greet_with_name("fran")


def greet_with(name, location):
    print(f"hello {name}")
    print(f"hello1 {location}")
    print("hello2")

greet_with("fran","Valencia")