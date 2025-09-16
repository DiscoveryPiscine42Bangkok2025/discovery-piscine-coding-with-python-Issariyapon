import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    cnt = s.count("z")
    print("z" * cnt if cnt > 0 else "none")

# python string_are_arrays.py "Zaz visits the zoo with Zazie"