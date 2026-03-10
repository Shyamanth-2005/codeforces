def process(n, nums):
  mx = max(nums)
  sm = 0
  for num in nums:
    sm += mx - num
  
  return sm


def main():
  n = int(input())
  nums = list(map(int,input().split()))

  res = process(n,nums)
  print(res)

if __name__ == "__main__":
  main()