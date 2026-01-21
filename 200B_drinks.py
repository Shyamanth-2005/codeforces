def main():
  n = int(input())
  percentages = list(map(int,input().split()))
  sum_per = sum(percentages)
  frac = sum_per/(n*100)
  print(round(frac*100,12))


if __name__ == "__main__":
  main()