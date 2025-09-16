def upcase_it(*args):
    if len(args) < 1:
        print("none")
    else:
        for i in range(len(args)):
            print(args[i].upper())

upcase_it("hello")