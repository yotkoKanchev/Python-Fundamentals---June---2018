import re

data = input()
pattern = r"""\b(?P<day>\d{2})(?P<sep>[/.-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"""
matches = re.finditer(pattern,data)

for match in matches :

    day = match.group('day')
    month = match.group('month')
    year = match.group("year")

    print(f"Day: {day}, Month: {month}, Year: {year}")

