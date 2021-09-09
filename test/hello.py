# str = input()
# age = int(input())
# score = float(input())
# print(str, age, score)

# first_name, last_name = input().split()
# print(first_name, last_name)

# year, month = map(int, input().split())
# print(year, month)

# list = []
# list2 = [1, 2, 3, True, False]
# list3 = [(1, 2, 3), {'name': 'user'}, [1, 2, 3]]
# list4 = [list, list2]
# print(list, list2)
# print(list3)
# print(len(list4), list4)

# list = [0, 1, 2, 3, 4, 5]
# print(list.index(2))
# list.insert(3, -1)
# print(list)
# list.append(6)
# print(list)
# list.extend([7, 8])
# print(list)
# list.sort()
# print('sort', list)
# list.sort(reverse=True)
# print('reverse sort', list)
# list.reverse()
# print('reverse', list)

# list = [1, 2, 3, 4, 5]
# del list[1]
# print(list)
# list.remove(1)
# print(list)

# list = [0, 1, 2, 3, 4, 5, 6, 7]
# print(list[len(list)-1])
# print(list[-1])

rect = (10, 10, 100, 100)
rect2 = 20, 20, 50, 50
print(type(rect), type(rect2))
print(rect[1])
print(rect2)

first = 'Hello "YOU"'
second = "Hello 'YOu'"
multi1 = '''Hello
friend'''
multi2 = """Hello
friend"""
print(first, second)
print(first[0], second[0])
print(multi1)
print(multi2)
