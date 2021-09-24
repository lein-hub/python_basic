def solution(n, m):
    def gcd(n, m):
        if m == 0:
            return n
        return gcd(m, n % m)

    def lcm(n, m):
        o = gcd(n, m)
        return o * (n / o) * (m / o)

    return [gcd(n, m), lcm(n, m)]
