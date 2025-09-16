import sys

args = sys.argv[1:]
if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for s in args:
        print(f"{s}: {len(s)}")
