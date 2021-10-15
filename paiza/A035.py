from itertools import combinations as cb

count = int(input())
scores = []
for i in range(count):
    scores.append(int(input()))

result = set()

for i in range(len(scores)+1):
    for x in list(cb(scores, i)):
        if x is not None:
            result.add(sum(x))


result = sorted(list(result))

print(len(result))
for i in result:
    print(i)
