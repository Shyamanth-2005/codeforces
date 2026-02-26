def _sum(n: int) -> int:
  b = n % 10
  n //= 10
  a = n % 10
  return a + b

def main():
  t = int(input())

  while t > 0:

    n = int(input())
    res = _sum(n)
    print(res)

    t -= 1
  
if __name__ == "__main__":
  main()