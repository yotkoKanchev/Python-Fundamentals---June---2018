import re

pattern = r'\d{2}-(?P<month>[A-Z][a-z]{2})-\d{4}'

string = '22-Jan-2015 22/Mar-1994 22-Mar-1995'

a = re.search(pattern, string)

print(a)