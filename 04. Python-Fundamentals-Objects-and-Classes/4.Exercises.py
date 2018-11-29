class Exercise:
    def __init__(self,topic, course, link, problems):
        self.topic = topic
        self.course = course
        self.link = link
        self.problems = problems

list = []
data = input()

while data != "go go go":
    exer_data = data.split(" -> ")
    exersise = Exercise(exer_data[0], exer_data[1], exer_data[2], exer_data[3].split(", "))
    list.append(exersise)
    data = input()

for item in list:
    print(f"Exercises: {item.topic}")
    print(f'Problems for exercises and homework for the "{item.course}" course @ SoftUni.')
    print(f"Check your solutions here: {item.link}")

    for j in range(0, len(item.problems)):
        print(f"{j+1}. {item.problems[j]}")


