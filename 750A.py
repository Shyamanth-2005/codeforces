def main():
  n,k = list(map(int,input().split()))
  total_time = 240
  i =1
  q = 0
  while i <= n:
    total_time -= i * 5
    if total_time >= k:
      q+= 1
    i +=1 

  
  print(q)




if __name__ == "__main__":
  main()