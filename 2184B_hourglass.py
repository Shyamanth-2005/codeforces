def main():
  t = int(input())
  # s - number of minutes the hourglass measures
  # k - the number of minutes after which the hourglass flips
  # m - the number of minutes after which Vadim will leave for errands
  while t > 0:
    s,k,m = list(map(int,input().split()))

    N = m // k
    if s < k:
      A = s
    else:
        if N % 2 == 0:
          A = s
        else:
          A = k
        
    dt = m - N * k
    ans = max(A - dt, 0)
    print(ans)
    t -= 1
  
if __name__  == "__main__":
  main()  