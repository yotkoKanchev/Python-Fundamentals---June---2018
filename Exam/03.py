import re
data = input()
match_list = []
while data != "make migrations":
    pattern = r"""((.*)(?P<name>[A-Z][a-z]+ [A-Z][a-z]+)(.*) (?P<age>\d{2}) (.*) (?P<data>\d{2}-\d{1,2}-\d{4}).)"""

    matches = re.finditer(pattern,data)

    for match in matches:
        match_list.append(match.group())

    for match in matches:

        name = match.group("name")
        age = match.group("age")
        data = match.group("data")
        print(f"{name}-{age}-{data}")
    data = input()



