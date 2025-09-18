import sys

args = sys.argv[1:]
if len(args) < 2:
    print("none")
else:
    for s in reversed(args):
        print(s)

# python aff_rev_params.py "Python"
# python aff_rev_params.py "Python" "piscine" "hello"