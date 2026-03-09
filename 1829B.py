def process(n, arr):
  cnt = 0
  icnt = 0
  i = 0
  while i < n:
    if arr[i] == 1:
      cnt = max(cnt,icnt)
      icnt = 0
    if arr[i] == 0:
      icnt += 1
      cnt = max(cnt,icnt)
    
    i += 1
  
  return cnt

def main():
  t = int(input())

  while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    res = process(n,arr)
    print(res)

    t -= 1

if __name__ == "__main__":
  main()
  # process(5,[1,0,0,1,0])
  # process(1,[0])
  # process(3,[0,0,0])
  # process(8,[0,0,0,1,0,0,0,0])