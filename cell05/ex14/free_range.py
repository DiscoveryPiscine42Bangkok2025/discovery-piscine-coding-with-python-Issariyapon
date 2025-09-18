import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        start, end = (a, b) if a <= b else (b, a)
        nums = list(range(start, end + 1))
        print(nums)
    except ValueError:
        print("none")

# python free_range.py 10 14
# python free_range.py 1 5