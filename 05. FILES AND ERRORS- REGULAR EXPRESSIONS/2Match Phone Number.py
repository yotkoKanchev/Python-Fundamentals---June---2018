import re

data = input()

pattern = r"""\+359(-| )2\1\d{3}\1\d{4}\b"""
matches = re.finditer(pattern,data)

for match in matches:
    print(match.group(), end=" ")