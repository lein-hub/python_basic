def solution(s):
    def strangify(word):
        result_list = list(word)
        for i in range(len(result_list)):
            if i % 2 == 0:
                result_list[i] = result_list[i].upper()
            else:
                result_list[i] = result_list[i].lower()
        return ''.join(result_list)

    ls = [i for i in s.split(" ")]

    for i in range(len(ls)):
        ls[i] = strangify(ls[i])

    return ' '.join(ls)


print(solution('try hello world'))
