n = 0
m = 0
while n != 11:
    print(f"Table de {n}: ", end="")
    while  m != 11:
        print(f"{n*m}", end=" ")
        m = m + 1
    print()
    n = n + 1
    m = 0