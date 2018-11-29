import re

data = input()

pattern = r"""\b(?:0x)?[0-9A-F]+\b"""
matches = re.finditer(pattern,data)

for match in matches:
    print(match.group(), end=" ")