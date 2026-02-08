def main():
  t = int(input())
  
  while t > 0:
    nums = list(map(int,input().split()))
    prim = max(nums)
    rest = sum(nums) - prim
    if prim == rest:
      print("YES")
    else:
      print("NO")


    t -= 1

if __name__ == "__main__":
  main()