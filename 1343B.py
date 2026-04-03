import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if (n // 2) % 2 != 0:
        print("NO")
        continue
    
    print("YES")
    
    k = n // 2
    
    # even numbers
    evens = [2 * i for i in range(1, k + 1)]
    
    # first k-1 odd numbers
    odds = [2 * i - 1 for i in range(1, k)]
    
    # last odd
    last = sum(evens) - sum(odds)
    odds.append(last)
    
    print(*evens, *odds)