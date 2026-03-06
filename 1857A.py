
def main():
   t = int(input())


   while t > 0:
    n = int(input())
    nums = list(map(int,input().split()))
    if sum(nums) %  2 == 0:
      print("YES")
    else:
      print("NO")
    t -= 1


if __name__ == "__main__":
  main()
  