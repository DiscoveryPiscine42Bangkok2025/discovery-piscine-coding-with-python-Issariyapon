num_1st = int(input("Enter the first number: "))
num_2nd = int(input("Enter the second number: "))
multi_result = num_1st * num_2nd

print(f"{num_1st} x {num_2nd} = {multi_result}")
if multi_result < 0:
    print("The result is negative.")
elif multi_result == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")