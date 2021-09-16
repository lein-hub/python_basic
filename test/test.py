# 1152번 문제
print(len(input().split()))

# 1157번 문제
list = list(input().upper())
set = {x for x in list}
dict = {}
result = ''
maxCount = 0
for x in set:
    dict[x] = 0
for x in list:
    dict[x] += 1
for x in dict:
    if result is None:
        result = x
        maxCount = dict[x]
    elif maxCount == dict[x]:
        result = '?'
    elif maxCount < dict[x]:
        result = x
        maxCount = dict[x]
print(result)

# 1271번 문제
n, m = map(int, input().split())
print(n // m)
print(n % m)

# 1302번 문제
n = int(input())
list = []
for x in range(n):
    list.append(input())
set = {x for x in list}
dict = {}
result = ''
maxCount = 0
for x in set:
    dict[x] = 0
for x in list:
    dict[x] += 1

result_list = []
for x in dict:
    if len(result_list) == 0:
        result_list = [x]
        maxCount = dict[x]
    elif maxCount == dict[x]:
        result_list.append(x)
    elif maxCount < dict[x]:
        result_list = [x]
        maxCount = dict[x]
result_list.sort()
print(result_list[0])

# 1764번 문제
n, m = map(int, input().saplit())
heard = []
saw = []
for x in range(n):
    heard.append(input())
for x in range(m):
    saw.append(input())
heard_saw = []
set = {x for x in heard}
for x in saw:
    count = len(set)
    set.add(x)
    if count == len(set):
        heard_saw.append(x)

print(len(heard_saw))
heard_saw.sort()
for x in heard_saw:
    print(x)
