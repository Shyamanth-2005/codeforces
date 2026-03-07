def main():
  t = int(input())

  while t > 0:
    n,k = list(map(int,input().split()))
    nums =  list(map(int,input().split()))

    if k in nums:
      print("YES")
    else:
      print("NO")
    t -= 1

if __name__ == "__main__":
  main()