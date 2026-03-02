def spy_detector(n: int, arr: list[int]) -> int:
  counter = dict()
  for num in arr:
    if num not in counter:
      counter[num] = 1
    else:
      counter[num] += 1
  
  for k,v in counter.items():
    if v == 1:
      idx = arr.index(k)
      return idx + 1
    


def main():
  t = int(input())

  while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    res = spy_detector(n,arr)
    print(res)

    t -= 1

if __name__ == "__main__":
  main()
  
