n = int(input())
m = int(input())

line = []

for i in range(n):
    line.append('*')

line = ''.join(line)

for i in range(m):
    print(line)
