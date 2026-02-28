
# [n * +ve nums]
# i and j i != j and abs(a - b) <= 1
# and remove the smallest testcase and if = then remove any one

def process(n: int, nums: list[int]) -> str:
  nums.sort()
  for i in  range(1,n):
    if nums[i] - nums[i - 1] > 1:
      return "NO"
  
  return "YES"

def main():
  t = int(input())


  while t > 0:
    n = int(input())
    nums = list(map(int,input().split()))
    res = process(n,nums)
    print(res)


    t -= 1
if __name__ == "__main__":
  main()