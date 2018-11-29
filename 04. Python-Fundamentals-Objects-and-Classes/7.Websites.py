class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries

websites_list = []

data = input()
while data != "end":
    spl_data = data.split(" | ")
    host_name = spl_data[0]
    domain_name = spl_data[1]


    if len(spl_data) > 2:
        queries = spl_data[2].split(",")
        website = Website(host_name,domain_name,queries)
    else:
        website = Website(host_name, domain_name, None)

    websites_list.append(website)

    data = input()

for j in websites_list:
    print(f"https://www.{j.host}.{j.domain}", end="")
    if j.queries != None:
        print(f"/query?=", end="")
        print(f"[", end="")
        print("]&[".join(j.queries), end="")
        print("]")


