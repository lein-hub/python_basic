def solution(food_times, k):
    minimum_stack = 0
    sorted_times = sorted(food_times)
    sorted_index = 0
    length = len(food_times)
    while k > 0:
        nums_minimum = 1
        minimum = sorted_times[sorted_index]
        for i in sorted_times[1:]:
            if i == minimum:
                nums_minimum += 1
            else:
                break

        if k > (minimum - minimum_stack) * (length):
            k -= (minimum - minimum_stack) * (length)

            sorted_index += nums_minimum
            length -= nums_minimum
            minimum_stack = minimum

        else:
            return k % length + 1


print(solution([3, 1, 2], 5)
      )
