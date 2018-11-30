data = input()
my_dict = {}

while data != "on work":

    args = data.split("->")
    book_details = args[0].split(" ")
    list_chapters = []
    list_chapters.append(len(args[1].split(', ')))

    title = book_details[0]
    author = book_details[1]

    price = float(book_details[2])

    list_chapters.insert(0, price)

    if author not in my_dict:
        my_dict[author] = {}
        my_dict[author][title] = list_chapters


    data = input()

new_data = input()
asked_list = []
while new_data!= "end work":
    asked_list.append(new_data)
    new_data = input()

print(my_dict)
res_list = []
for item in asked_list:
    if item not in my_dict:
        print("NO")
    else:
        res_list.append(item)

print(res_list)