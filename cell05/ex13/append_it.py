import sys, re

args = sys.argv[1:]
if not args:
    print("none")
else:
    for w in args:
        if not re.search(r'ism$', w):
            print(w + "ism")

# python append_it.py "parallel" "egoism" "human"