t = ()

n = input("Enter the number of ints: ")
n = int(n)

line = input()
line_elements = line.split(" ")

for i in range (n):
    a=line_elements[i]
    a=int(a)
    t=t+(a,)

print(hash(t))