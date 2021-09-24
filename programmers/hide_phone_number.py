def solution(phone_number):
    answer = ''
    stripped_number = list(phone_number)
    stripped_number.reverse()

    for i in range(len(stripped_number)):
        if i > 3:
            stripped_number[i] = '*'

    stripped_number.reverse()
    answer = answer.join(stripped_number)

    return answer


print(solution("01033334444"))
