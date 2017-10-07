import os
import re
a = open('actual_data.txt', "r+")
x = a.read()
y = re.findall('[0-9]+',x)
total = 0
for i in y:
    total += int(i)
print(total)
