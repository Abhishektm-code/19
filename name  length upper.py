def greet_user():
    name = input("Please enter your name: ")
    
    print(f"Hello, {name}")
    
    print(f"Your name has {len(name)} characters.")
    
    print(f"Your name in uppercase: {name.upper()}")

greet_user()