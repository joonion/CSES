def solve(n):
    s = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        s.append(n)
    print(" ".join(map(str, s)))
        
n = int(input())
solve(n)