import re
#{'Order Number': 123, 'Customer': 'John Doe', 'Items': {'Item 1': 2, 'Item 2': 1, 'Item 3': 3}}
# ['Order', '123', 'John', 'Doe', 'Itema', 'Itemb', 'Itemc']

with open('textregex.txt') as f:
    for line in f:
        match = re.findall(r"\w+", line)
        dictio = {'Order Number': match[1], 'Customer': match[], 'Items': {'Item 1': 2, 'Item 2': 1, 'Item 3': 3}}
        print(match)
