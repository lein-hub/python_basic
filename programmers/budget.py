def solution(d, budget):
    d.sort()

    result = []
    while len(d) and sum(result) < budget:
        result.append(d.pop(0))

    return len(result) - 1 if sum(result) > budget else len(result)
