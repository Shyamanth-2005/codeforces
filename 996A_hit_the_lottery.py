def main():
  n = int(input())
  count = 0
  while n > 0:
    if n > 100:
      q = n // 100
      n -= (q * 100)
      count += q
    elif n >= 20:
      q = n // 20
      n -= (q*20)
      count += q
    elif n >= 10:
      q = n // 10
      n -= (q*10)
      count += q
    elif n >= 5:
      q = n// 5
      n -= (q*5)
      count += q
    else:
      count += n
      n = 0
  print(count)
if __name__ == "__main__":
  main()

  