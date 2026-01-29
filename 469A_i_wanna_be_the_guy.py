def main():
  n = int(input())
  x = set(map(int,input().split()[1:]))
  y = set(map(int,input().split()[1:]))
  res = x.union(y)
  for i in range(1,n+1):
    if i not in res:
      return "Oh, my keyboard!"
  
  return "I become the guy."



if __name__ == "__main__":
  res = main()
  print(res)