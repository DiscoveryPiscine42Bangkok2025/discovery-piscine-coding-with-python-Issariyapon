def downcase_it(*args):
    if len(args) < 1:
        print("none")
    else:
        for i in range(len(args)):
            print(args[i].lower())

downcase_it()
downcase_it("HELLO WORLD")
downcase_it("HELLO", "WORLD")