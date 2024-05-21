def greet(name="World", language="English"):
    if language == "English":
        print(f"Hello, {name}!")
    elif language == "Spanish":
        print(f"Hola, {name}!")
    else:
        print("Invalid language.")
greet()
greet(name="John")
