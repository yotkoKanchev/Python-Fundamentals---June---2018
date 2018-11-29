import re

data = input()

pattern = r"""(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"""

matches = re.finditer(pattern, data)

for match in matches:

    print(match.group(), end=" ")