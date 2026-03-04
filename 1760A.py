def get_median(nums: list[int]) -> int:
  nums.sort()
  return nums[1]


def main():
  t = int(input())

  while t > 0:
    nums = list(map(int,input().split()))
    res = get_median(nums)
    print(res)
    t -= 1

if __name__ == "__main__":
  main()