import re

with open('textregex.txt') as f:
    for line in f:
        match = re.serch(r"/w+")
        print(match)
