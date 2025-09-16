import sys

def shrink(s: str) -> None:
    print(s[:8])

def enlarge(s: str) -> None:
    print(s + "Z" * (8 - len(s)))

args = sys.argv[1:]
if not args:
    print("none")
else:
    for a in args:
        n = len(a)
        if n > 8:
            shrink(a)
        elif n < 8:
            enlarge(a)
        else:
            print(a)

# python methods_everywhere.py 'lol' 'physically' 'backpack'