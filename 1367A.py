def main():
  b = input()
  if len(b) == 2:
    return b
  # abac
  # 0123
  # ab ba ac
  # 01 12 23
  # res = ""
  
  # for i in range(0,len(b),2):
  #   res += b[i]
  res = b[0:len(b):2]
  
  
  res += b[-1]
  return res

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    res = main()
    print(res)
