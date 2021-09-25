# def solution(n):
#     def isPrime(n):
#         if n != 2 and n % 2 == 0:
#             return False
#         for a in range(2, n//2+1):
#             if n % a != 0:
#                 continue
#             else:
#                 return False
#         return True

#     answer = 0

#     for i in range(2, n+1):
#         if isPrime(i):
#             answer += 1
#     return answer

def solution(n):
    primes = set(i for i in range(2, n+1))

    for i in range(2, len(primes)):
        primes -= set(range(i*2, n+1, i))

    return len(primes)
