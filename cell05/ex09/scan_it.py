import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    cnt = text.count(keyword)
    print(cnt if cnt > 0 else "none")

# python scan_it.py "the"
# python scan_it.py "the" "the quick brown fox jumps over the lazy dog"