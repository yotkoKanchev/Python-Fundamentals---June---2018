import re

data = input()

pattern = r"""\b[A-Z][a-z]+ [A-Z][a-z]+\b"""
matches = re.findall(pattern, data)

for match in matches:
    print(match, end=" ")