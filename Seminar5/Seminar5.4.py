n = input("Enter the number of values in set: ")
n = int(n)

line = input()
line_elements = line.split(" ")

for i in range (0,n):
    line_elements[i]=int(line_elements[i])

set = set(line_elements)

print(sum(set)/len(set))