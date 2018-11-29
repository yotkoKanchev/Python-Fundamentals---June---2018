data = input()
dict = {}
while data != 'shopping time':
    stock_data = data.split(" ")
    stock_product = stock_data[1]
    stock_quantity = int(stock_data[2])

    if stock_product not in dict:
        dict[stock_product] = stock_quantity
    else:
        stock_quantity += dict[stock_product]
        dict[stock_product] = stock_quantity

    data = input()

data = input()

while data != "exam time":
    buy_data = data.split(" ")
    buy_product = buy_data[1]
    buy_quantity = int(buy_data[2])

    if buy_product not in dict:
        print(f"{buy_product} doesn't exist")
    elif dict[buy_product] <= 0:
        print(f"{buy_product} out of stock")
    else:
        dict[buy_product] = dict[buy_product] - buy_quantity
                  

    data = input()

for key, value in dict.items():
    if value > 0:
        print(f"{key} -> {value}")