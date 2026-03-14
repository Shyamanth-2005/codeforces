def main():
  t = int(input())

  for _ in range(t):
    n, x = list(map(int, input().split()))
    stations = list(map(int,input().split()))

    prev = 0
    mx_gap = 0

    for s in stations:
      mx_gap = max(mx_gap, s - prev)
      prev = s

    mx = max(mx_gap, 2 * (x - stations[-1]))

    print(mx)

if __name__ == "__main__":
  main()
  
