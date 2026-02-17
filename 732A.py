def main():
  k,r = list(map(int,input().split()))
  i = 1
  count = 0
  temp = k
  if k % 10 == r or k % 10 == 0:
    return count + 1

  while temp % 10 != r and temp % 10 != 0:

    temp = k * i
    i += 1
    count += 1
  
  return count


if __name__ == "__main__":
  res = main()
  print(res)