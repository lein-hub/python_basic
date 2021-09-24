def solution(nums):
    answer = 0
    for i in range(len(nums)):
        x = nums[i]
        for j in range(i+1, len(nums)):
            y = nums[j]
            for k in range(j+1, len(nums)):
                z = nums[k]
                sum = x + y + z
                isPrime = True
                for a in range(2, sum//2):
                    if sum % a != 0:
                        continue
                    else:
                        isPrime = False
                        break
                if isPrime:
                    answer += 1
    return answer
