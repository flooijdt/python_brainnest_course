import re
#{'Order Number': 123, 'Customer': 'John Doe', 'Items': {'Item 1': 2, 'Item 2': 1, 'Item 3': 3}}
# ['Order', '123', 'John', 'Doe', 'Itema', 'Itemb', 'Itemc']

with open('textregex.txt') as f:
    for line in f:
        match = re.findall(r"\w+", line)
        items = [i for i in match[4:]]
        items_dict = {items.index(i): i for i in items}
        dictio = {'Order Number': match[1], 'Customer': match[2] + ' ' +
                  match[3], 'Items': items_dict}
        with open('regex_output.txt', 'a') as o:
            o.write(dictio)


with open('regex_output.txt') as f:
    print(r.read())