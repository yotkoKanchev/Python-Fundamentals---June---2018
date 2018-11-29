import operator
class Bank_account:
    def __init__(self, bank, name, balance):
        self.bank = bank
        self.name = name
        self.balance = balance
list = []
data = input()
while data != "end":

    spl_data = data.split(" | ")
    account = Bank_account(spl_data[0], spl_data[1], float(spl_data[2]))
    list.append(account)
    data = input()

sorted_bank = sorted(list, key=operator.attrgetter("bank"))
sorted_list = sorted(sorted_bank, key=operator.attrgetter("balance"), reverse=True)

for item in sorted_list:
    print(f"{item.name} -> {float(item.balance):.2f} ({item.bank})")