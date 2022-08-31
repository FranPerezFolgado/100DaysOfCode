

def calculate(a,b,operation):
    
    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    def sum(a,b):
        return a + b

    def subtract(a,b):
        return a - b

    operations = {
        "+":sum,
        "-":subtract,
        "/":divide,
        "*":multiply
    }
    return operations[operation](a,b)