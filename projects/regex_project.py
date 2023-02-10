#!/bin/python3
# author: Camilo Pimentel
# date_created: 10/02/2023
# last_modified: 10/02/2023

# description:
# Takes a 'textregex.txt' file with customer data as input and
# outputs a 'regex_output.txt' with organized customer data.

import re

try:
    with open('textregex.txt') as f:
        for line in f:
            match = re.findall(r"\w+", line)
            items = [i for i in match[4:]]
            items_dict = {items.index(i): i for i in items}
            dictio = {'Order Number': match[1], 'Customer': match[2] + ' ' +
                      match[3], 'Items': items_dict}
            with open('regex_output.txt', 'a') as o:
                o.write(str(dictio)+'\n')
except OSError:
    print("Could not open designated file to read.")

try:
    with open('regex_output.txt') as f:
        for line in f:
            print(f.read())
except OSError:
    print("Could not write output to file.")
