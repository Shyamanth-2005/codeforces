def main():
  r,b = list(map(int,input().split()))
  max_days = min(r,b)
  remaining_socks = max(r,b) - min(r,b)
  no_same_socks = remaining_socks // 2
  print(max_days,no_same_socks)


if __name__ == "__main__":
  main()