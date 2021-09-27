def solution(lottos, win_nums):
    zero = lottos.count(0)
    correct = 0
    for i in win_nums:
        if lottos.__contains__(i):
            correct += 1

    least_potential = 6 if correct < 2 else 7 - correct
    most_potential = 6 if correct + zero < 2 else 7 - correct - zero
    return [most_potential, least_potential]
