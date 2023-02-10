import re

with open('textregex.txt') as f:
    for line in f:
        match = re.search(r"/w+", line)
        print(match)
