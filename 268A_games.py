def main():
  n = int(input())
  N = n
  count = 0
  home = []
  away = []

  while n > 0:
    h,a = list(map(int,input().split()))
    home.append(h)
    away.append(a)
    n -= 1
  
  for i in range(N):
    for j in range(N):
      if i != j and home[i] == away[j]:
        count += 1
  
  print(count)


    
    



if __name__ == "__main__":
  main()