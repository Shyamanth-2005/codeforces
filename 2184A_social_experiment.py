def sub_fun(n):
  if n == 2:
    return 2
  elif n == 3:
    return 3
  elif n % 2 == 0:
    return 0
  else:
    return 1
def main():
  t = int(input())
  while t > 0:
    n = int(input())
    res = sub_fun(n)
    print(res)
    t -= 1



if __name__ == "__main__":
  main()