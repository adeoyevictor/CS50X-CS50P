lst = {}

while True:
    try:
        item = input("Item: ").upper()
        if item in lst:
            lst[item] += 1
        else:
            lst[item] = 1
    except EOFError:
        print()
        break


dict(sorted(lst.items()))

for item in dict(sorted(lst.items())):
    print(item)
