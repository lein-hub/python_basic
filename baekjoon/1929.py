start, end = map(int, input().split())
if start < 2:
    start = 2
primes = set(a for a in range(start, end+1))

for i in range(2, end+1):
    primes -= set(range(i*2, end+1, i))


for i in sorted(list(primes)):
    print(i)
