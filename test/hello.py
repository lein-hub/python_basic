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

# rect = (10, 10, 100, 100)
# rect2 = 20, 20, 50, 50
# print(type(rect), type(rect2))
# print(rect[1])
# print(rect2)

# first = 'Hello "YOU"'
# second = "Hello 'YOu'"
# multi1 = '''Hello
# friend'''
# multi2 = """Hello
# friend"""
# print(first, second)
# print(first[0], second[0])
# print(multi1)
# print(multi2)
# print(multi1, multi2)

# str = 'hello my friend'
# split_default = str.split()
# split_char = str.split('e')
# print(split_default)
# print(split_char)
# str_list = list(str)
# print(str_list)
# joined_empty = ''.join(str_list)
# joined_char = '-'.join(str_list)
# print(joined_empty)
# print(joined_char)

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sub1 = list[5:8]
# sub2 = list[7:]
# sub3 = list[:4]
# sub4 = list[::2]
# print(sub1)
# print(sub2)
# print(sub3)
# print(sub4)

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sub5 = list[:-3]
# sub6 = list[-5:]
# sub7 = list[::-1]
# sub8 = list[8:3:-1]
# sub9 = list[-2:-4:-1]
# print(sub5)
# print(sub6)
# print(sub7)
# print(sub8)
# print(sub9)

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list)
# del list[:3]
# print(list)
# del list[2:5]
# print(list)
# list[1:3] = [100, 200]
# print(list)

# # 사용자로부터 값을 입력받아 앞의 3자리, 뒤의 3자리를 출력하는 코드를 작성하라(단 사용자는 3자리 이상 입력한다)
# list = list(input())
# print(list[:3], list[-3:])

# capitals = {'Korea': 'Seoul', 'United Kingdom': 'London'}
# print(capitals['Korea'])
# capitals['Japan'] = 'Tokyo'
# print(capitals)
# capitals.update({'USA': 'Washington, D.C.', 'China': 'Beijing'})
# print(capitals)
# del capitals['USA']
# print(capitals)

# set1 = set([1, 2, 3, 4])
# set2 = {(1, 2), 2, 3, 'Hello'}
# print(set1)
# set1.add(5)  # 하나 추가
# print(set1)
# set1.add(1)  # 이미 존재하는 값
# print(set1)
# set1.remove(4)
# print(set1)
# set1.update([7, 8])  # 여러개 추가
# print(set1)
# print(set1 & set2)  # 교집합, set1.intersection(set2)
# print(set1 | set2)  # 합집합, set1.union(set2)
# print(set1 - set2)  # 차집합, set1.difference(set2)


while True:
    print('Enter Number', end=' ')
    value = int(input())
    if value < 0:
        break
