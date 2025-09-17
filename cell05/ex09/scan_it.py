import sys
import re

args = sys.argv[1:]
if len(args) != 2:
    print("none")
else:
    keyword = args[0]
    text = args[1]

    pattern = f'(?={keyword})'
    matches = re.findall(pattern, text)
    if not matches:
        print("none")
    else:
        print(len(matches))




