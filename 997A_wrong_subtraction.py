def main():
  n,k = list(map(int,input().split()))
  while k > 0:
    last_dig = n % 10
    if last_dig != 0:
      n -= 1
    else:
      n //= 10
    k -= 1
  return n

if __name__ == "__main__":
  res = main()
  print(res)