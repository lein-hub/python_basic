def solution(food_times, k):
    minimum_stack = 0
    sorted_times = [(0,0) for _ in len(food_times)]
    for i in range(len(food_times)):
        sorted_times[i] = (food_times[i], i)
    sorted_times.sort(key=lambda x : (x[0], x[1]))
    
    sorted_index = 0
    length = len(food_times)
    while k > 0:
        minimum, _ = sorted_times[sorted_index]

        if k > (minimum - minimum_stack) * (length):
            k -= (minimum - minimum_stack) * (length)

            sorted_index += 1
            length -= 1
            minimum_stack = minimum

        else:
            return k % length + 1


print(solution([3, 1, 2], 5)
      )
