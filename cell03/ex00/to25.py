num = int(input("Enter a number less than 25: "))

if num > 25:
    print("Error")
else:
    while num != 26:
        print("Inside the loop, my variable is", num)
        num = num + 1
