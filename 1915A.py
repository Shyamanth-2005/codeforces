# def process(nums: list[int]) -> int:
#   cntr = dict()
#   for num in nums:
#     if num not in cntr:
#       cntr[num] = 1
#     else:
#       cntr[num] += 1
  
#   for k,v in cntr.items():
#     if v == 1:
#       return k
  


def main():
  t = int(input())

  while t > 0:
    a,b,c = map(int,input().split())
    res = a ^ b ^ c # xor property for getting the odd one out 
    print(res)
    t -= 1
  

if __name__ == "__main__":
  main()
