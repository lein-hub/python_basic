def solution(price, money, count):
    price = sum([i*price for i in range(1, count+1)])
    return price - money if price - money > 0 else 0
