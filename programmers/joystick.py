def solution(name):
    initial = ['A' for _ in range(len(name))]
    movement = 0
    for i, n in zip(initial, name):
        distance = abs(ord(i)-ord(n))
        if distance <= 13:
            movement += distance
        else:
            little_one = ord(min([i, n])) - ord('A')
            big_one = ord(max([i, n])) - ord('A')
            movement += ord('Z') - big_one + little_one

    return movement


print(solution('JEROEN'))
