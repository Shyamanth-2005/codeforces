def main():
  n = int(input())
  count = 0
  while n > 0:
    p , q = list(map(int,input().split()))
    remaining_space = q -p 
    if remaining_space >= 2 :
      count += 1
    n -= 1
  print(count)



if __name__ == "__main__":
  main()