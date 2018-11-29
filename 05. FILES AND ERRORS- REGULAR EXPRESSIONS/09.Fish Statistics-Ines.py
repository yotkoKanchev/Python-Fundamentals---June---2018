import re

data = input()

pattern = r"""(?P<tail>>*)<(?P<body>\(+)(?P<eye>[-'x])>"""
fish_matches = list(re.finditer(pattern, data))

tail_type = "None"
tail_cm = None
body_type = None
status = None
counter = 1

if not fish_matches:
    print("No fish found")
else:

    for fish_match in fish_matches:
        tail_len = len(fish_match.groupdict()['tail'])
        body_len = len(fish_match.groupdict()['body'])
        fish_eye = fish_match.groupdict()['eye']
        if tail_len > 5:
            tail_type = 'Long'
        elif tail_len > 1:
            tail_type = 'Medium'

        elif tail_len == 1:
            tail_type = 'Short'
        tail_cm = tail_len * 2

        if body_len > 10:
            body_type = "Long"
        elif body_len > 5:
            body_type = 'Medium'
        else:
            body_type = "Short"

        if fish_eye == "'":
            status = "Awake"
        elif fish_eye == "-":
            status = "Asleep"
        else:
            status = "Dead"

            # bez printovete !!!!!!!
