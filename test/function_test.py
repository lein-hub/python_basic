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


def merge(ls1, ls2):
    result = []
    while True:
        if len(ls1) == 0:
            return result.extend(ls2)
        if len(ls2) == 0:
            return result.extend(ls1)

        if ls1[0] > ls2[0]:
            result.append(ls2.pop(0))
        else:
            result.append(ls1.pop(0))


def merge_sort(list):
    if len(list) > 1:
        ls1 = merge_sort(list[:len(list)//2])
        ls2 = merge_sort(list[len(list)//2:])
        return merge(ls1, ls2)

    return list


ls = [1, 6, 23, 5, 23, 5, 12, 6, 3]

print(merge_sort(ls))


# ls = [1]
# ls.pop()
# print(len(ls))
