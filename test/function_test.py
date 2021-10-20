# ls = []


# def put(val):
#     global ls
#     return ls.append(val)


# def get():
#     global ls
#     return ls.pop(0)


# ----------------------------------------

# ls = [1, 3, 6, 9, 12, 15, 18, 21]


# def find(val, start=0, end=len(ls)-1):
#     global ls
#     center = int((end + start) / 2)
#     if start > end:
#         return 'fail'
#     if ls[center] > val:
#         end = int(end / 2)
#         return find(val, start, end)
#     elif ls[center] < val:
#         start = center + 1
#         return find(val, start, end)
#     else:
#         return center


# print(find(20))

# ----------------------------------------

import random


def merge(ls1, ls2):
    result = []
    while True:
        if not ls1:
            result.extend(ls2)
            return result
        if not ls2:
            result.extend(ls1)
            return result

        if ls1[0] > ls2[0]:
            result.append(ls2.pop(0))
        else:
            result.append(ls1.pop(0))

# def merge(left, right):
#     result = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#         elif len(left) > 0:
#             result.extend(left)
#             break
#         else:
#             result.extend(right)
#             break
#     return result


def merge_sort(list):
    length = len(list)
    if length > 1:
        ls1 = merge_sort(list[:length//2])
        ls2 = merge_sort(list[length//2:])
        return merge(ls1, ls2)

    return list


ls = [random.randint(0, 200) for i in range(100000)]

print(merge_sort(ls))


# ls = [1]
# ls.pop()
# print(len(ls))
