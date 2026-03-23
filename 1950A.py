def main():
  a,b,c = list(map(int,input().split()))
  if a < b < c:
    print("STAIR")
  elif a < b > c:
    print("PEAK")
  else:
    print("NONE")

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    main()