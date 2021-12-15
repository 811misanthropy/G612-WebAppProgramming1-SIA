list = []

n = input("Enter the number of lines: ")
n = int(n)

for i  in range (n):
    line = input()
    line_elements = line.split(" ")
    op = line_elements[0]
    if op == "print":
        print(list)
    else:
        if op == "sort":
            list.sort()
        else:
            if op == "pop":
                list.pop()
            else:
                if op == "reverse":
                    list.reverse()
                else:
                    if op == "remove":
                        e = line_elements[1]
                        e=int(e)
                        list.remove(e)
                    else:
                        if op=="append":
                            e=line_elements[1]
                            e=int(e)
                            list.append(e)
                        else:
                            if op == "insert":
                                i = line_elements[1]
                                i=int(i)
                                e = line_elements[2]
                                e=int(e)
                                list.insert(i,e)
                            else:
                                print("Comanda neacceptat! Lista invalida!")
                                break
