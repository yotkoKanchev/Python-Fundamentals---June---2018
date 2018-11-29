text = input()
lookup_text = input()

occurrences = 0
current_index = 0

while current_index != -1:
    current_index = text.find(lookup_text, current_index)
    if current_index is not -1:
        occurrences += 1
        current_index += 1

print(occurrences)