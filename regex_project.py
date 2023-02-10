import re
#{'Order Number': 123, 'Customer': 'John Doe', 'Items': {'Item 1': 2, 'Item 2': 1, 'Item 3': 3}}

with open('textregex.txt') as f:
    for line in f:
        match = re.findall(r"\w+", line)
        dictio = {'Order'}
        print(match)
