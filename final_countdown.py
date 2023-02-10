#!/bin/python3
import time

count = int(input("Input the time to be counted down in seconds:\n"))
counter = count
for i in range(count):
    print(counter)
    time.sleep(1)
    counter -= 1