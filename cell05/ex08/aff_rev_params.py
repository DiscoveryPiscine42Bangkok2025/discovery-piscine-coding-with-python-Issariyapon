import sys

args = sys.argv[1:]
if len(args) < 2:
    print("none")
else:
    for s in reversed(args):
        print(s)

# python upcase_it.py "Python"
# python upcase_it.py "Python" "piscine" "hello"