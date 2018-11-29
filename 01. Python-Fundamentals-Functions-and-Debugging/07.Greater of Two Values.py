type = input()
first = input()
second = input()

if type == "int":
    def greater(num1,num2):
        if int(num1) > int(num2):
            return num1
        else:
            return num2
elif type == "char":
    def greater(char1,char2):
        if ord(char1) > ord(char2):
            return char1
        else:
            return char2
elif type == "string":
    def greater(str1, str2):
        if str1 > str2:
            return str1
        else:
            return str2

print(greater(first,second))