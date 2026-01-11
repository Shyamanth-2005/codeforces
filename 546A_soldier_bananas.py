def main():
  k,n,w = list(map(int,input().split()))
  # sum formula :natural numbers
  na_s = ((w)*(w+1))//2
  cost = k * na_s
  return max(0,cost-n)
  


if __name__ == "__main__":
  res = main()
  print(res)
  
  