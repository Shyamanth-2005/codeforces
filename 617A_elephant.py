def main():
  x = int(input())
  count = 0
  
  if x% 5 == 0:
    count = x // 5
  else:
    count = (x//5) + 1
  print(count)
  
  
if __name__ == "__main__":
  main()