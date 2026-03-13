def main():
  t = int(input())
  c_nums  = [1,2,3,4,5,6,7,8,9,10]
  mn = 10
  for _ in range(t):

    a,b = list(map(int,input().split()))

    mn = 10

    par_c_nums = c_nums[a-1:b]

    for c in par_c_nums:
      val = (c - a) + (b - c)
      mn = min(mn, val)
    
    print(mn)


if __name__ == "__main__":
  main()