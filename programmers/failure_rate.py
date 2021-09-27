def solution(N, stages):
    players = len(stages)
    rates = []
    for i in range(1, N+1):
        if players:
            rates.append((i, stages.count(i) / players))
            players -= stages.count(i)
        else:
            rates.append((i, 0))

    return [i[0] for i in sorted(rates, key=lambda x: x[1], reverse=True)]


print(solution(5, [4, 4, 4, 4, 4, 4, 4]))
