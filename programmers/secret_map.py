def solution(n, arr1, arr2):
    bin_arr1 = [list(format(i, 'b').rjust(n, '0').replace(
        '0', ' ').replace('1', '#')) for i in arr1]
    bin_arr2 = [format(i, 'b').rjust(n, '0').replace(
        '0', ' ').replace('1', '#') for i in arr2]

    for i in range(len(bin_arr2)):
        for j in range(len(bin_arr2[i])):
            if bin_arr2[i][j] == '#':
                bin_arr1[i][j] = '#'

    return [''.join(i) for i in bin_arr1]


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
