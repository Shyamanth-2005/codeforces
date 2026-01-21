def main():
  magnets = ""
  count = 0
  n = int(input())
  while n > 0:
    magnets += input()
    n -= 1
  # print(magnets[1])
  for i in range(1,len(magnets)):
    if magnets[i-1] == magnets[i]:
      count += 1
  return count+1

if __name__ =="__main__":
  res = main()
  print(res)

