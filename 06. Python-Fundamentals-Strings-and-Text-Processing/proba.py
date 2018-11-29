data = input()


while data != 'end':
    args = data.split(" - ")
    language = args[0]

    course = args[1].split(", ")[0]
    number = int(args[1].split(", ")[1])


    print(language)
    print(course)
    print(number)
    data = input()

