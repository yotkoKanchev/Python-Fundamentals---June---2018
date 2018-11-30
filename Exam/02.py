data =input()
import itertools


while data != "stop playing":
    result = ""
    args = list(map(int, data.split()))

    if len(args) > len(set(args)):
        print(f"Non-unique list: ", end="")
        for i in range(0, len(args)):
            if args[i ]% 2 != 0:
                args[i] +=3
        args.sort()
        print(":".join((map(str, args))))
        print(f"Output: {sum(args)/len(args):.2f}")
    else:
        print(f"Unique list: ",end = '')

        for i in range(0,len(args)):
            if args[i] % 2 == 0:
                args[i]+=2
        args.sort()
        print(",".join(map(str, args)))
        print(f"Output: {sum(args)/len(args):.2f}")




    data = input()



