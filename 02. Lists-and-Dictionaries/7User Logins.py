data = input()
dict = {}
while data != "login":
    acc_data = data.split(" -> ")
    name = acc_data[0]
    password = acc_data[1]
    dict[name] = password

    data = input()

data = input()
log_counter = 0
while data != "end":
    log_in_data = data.split(" -> ")
    log_name = log_in_data[0]
    log_pass = log_in_data[1]

    if log_name in dict:
        if dict[log_name] == log_pass:
            print(f"{log_name}: logged in successfully")
        else:
            print(f"{log_name}: login failed")
            log_counter+=1
    else:
        print(f"{log_name}: login failed")
        log_counter+=1

    data = input()
print(f"unsuccessful login attempts: {log_counter}")