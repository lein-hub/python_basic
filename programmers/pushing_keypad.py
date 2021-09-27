def solution(numbers, hand):
    current_left = '*'
    current_right = '#'

    result = []

    for i in numbers:
        if i in [1, 4, 7]:
            current_left = i
            result.append('L')
        elif i in [3, 6, 9]:
            current_right = i
            result.append('R')
        else:
            if distance(current_left, current_right, i, hand) == 'R':
                current_right = i
                result.append('R')
            else:
                current_left = i
                result.append('L')

    return ''.join(result)


def distance(left, right, target, hand):
    keypad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
    left_point = 0
    right_point = 0
    target_point = 0

    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if left == keypad[i][j]:
                left_point = [i, j]
            if right == keypad[i][j]:
                right_point = [i, j]
            if target == keypad[i][j]:
                target_point = [i, j]

    left_distance = abs(
        target_point[0] - left_point[0]) + abs(target_point[1] - left_point[1])
    right_distance = abs(
        target_point[0] - right_point[0]) + abs(target_point[1] - right_point[1])

    if left_distance == right_distance:
        return 'R' if hand == 'right' else 'L'
    elif left_distance < right_distance:
        return 'L'
    else:
        return 'R'
