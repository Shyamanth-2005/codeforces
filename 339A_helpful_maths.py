def main():
  nums = list(map(int,input().split("+")))
  nums = sorted(nums)
  nums = list(map(str,nums))
  print("+".join(nums))
  
if __name__ == "__main__":
  main()
  