def greetings(*args):
    if not args:
        print("Hello, noble stranger.")
        return

    for name in args:
        if isinstance(name, str):
            print(f"Hello, {name}.")
        else:
            print("Error! It was not a name.")


greetings()
greetings("Belle")
greetings(50)
            