student_grades = {
    'ivan': [3, 4],
    'petar': [5, 2, 5],
    'maria': [6, 6, 5, 6],
    'gosho': [5, 6]
}

sorted_by_value_than_key = sorted(student_grades.items(), key = lambda kvp: (-len(kvp[1]), kvp[0]))
print(sorted_by_value_than_key)

