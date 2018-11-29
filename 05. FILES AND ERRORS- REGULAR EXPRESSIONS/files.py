list_rows_odd = []
counter = 0
with open("file_to_read.txt", 'r') as r_file:
    rows = r_file.readlines()
    for row in rows:
        if not counter % 2 == 0:
            list_rows_odd.append(row)
        counter+=1

print(list_rows_odd)

with open('file_to_write.txt', 'w') as w_file:
    w_file.writelines   (list_rows_odd)