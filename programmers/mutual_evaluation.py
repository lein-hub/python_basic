def solution(scores):
    result = []
    num_of_scores = len(scores)
    for i in range(len(scores)):
        my_scores = [j[i] for j in scores]
        total = 0
        if my_scores.count(my_scores[i]) == 1 and (my_scores[i] == min(my_scores) or my_scores[i] == max(my_scores)):
            total = (sum(my_scores) - my_scores[i]) / (num_of_scores - 1)
        else:
            total = sum(my_scores) / num_of_scores

        if total >= 90:
            result.append('A')
        elif total >= 80:
            result.append('B')
        elif total >= 70:
            result.append('C')
        elif total >= 50:
            result.append('D')
        else:
            result.append('F')

    return ''.join(result)


print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
