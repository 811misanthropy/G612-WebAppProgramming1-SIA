n = input("Enter the number of scores: ")
n = int(n)
list0 = []
list = []
list0 = input().split(" ")
for i in range(n):
    list0[i] = int(list0[i])
    list.insert(i, list0[i])

list.sort()
i = i-1
a = list[i]
i=i-1
while a == list[i] and i != 0:
    i = i-1
print(list[i])