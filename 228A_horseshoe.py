def main():
  shoes = list(map(int,input().split()))
  unique_shoes = len(set(shoes))
  return 4 - unique_shoes

if __name__ == "__main__":
  res = main()
  print(res)