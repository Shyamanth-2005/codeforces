def main():
  n = int(input())
  opinons = list(map(int,input().split()))
  if any(opinons):
    return "HARD"
  return "EASY"

if __name__ == "__main__":
  res  = main()
  print(res)