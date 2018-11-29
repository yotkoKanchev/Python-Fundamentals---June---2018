import re

data = input()

pattern = r"""[2-9|JQKA][SHDC]|10[SHDC]"""
matches = re.findall(pattern,data)

for match in matches:
    print(match,end=" ")