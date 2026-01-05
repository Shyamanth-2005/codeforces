def main():
  x = 0
  n = int(input())
  while n > 0:
    inp = list(input())
    inp.pop(inp.index('X'))
    if inp[1] == "+":
      x += 1
    else:
      x -= 1
    n -= 1
  return x
    
if __name__ == "__main__":
  res = main()
  print(res)
  