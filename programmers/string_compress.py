def solution(s):
    if len(s) == 1:
        return 1

    compressed_list = []

    for n in range(1, len(s) // 2 + 1):
        chunked_list = [s[i:i+n] for i in range(0, len(s), n)]
        comparer = chunked_list[0]
        stacks = 1
        compressed_string = ''
        for i in chunked_list[1:]:
            if comparer == i:
                stacks += 1
            else:
                compressed_string += (str(stacks) if stacks > 1 else '') + \
                    comparer
                stacks = 1
                comparer = i

        compressed_string += (str(stacks) if stacks > 1 else '') + \
            comparer

        compressed_list.append(len(compressed_string))

    return min(compressed_list)


print(solution('ababcdcdababcdcd'))
