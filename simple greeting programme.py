# version 1
def greet():
    print("Hello!")

# version 2
def greet(name):
    print(f"Hello, {name}!")

# version 3
def greet(name="World"):
    print(f"Hello, {name}!")

# version 4
def greet(name="World", language="English"):
    if language == "English":
        print(f"Hello, {name}!")
    elif language == "Spanish":
        print(f"Hola, {name}!")
    else:
        print("Invalid language.")
