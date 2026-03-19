def is_prime(n: int) -> bool:
  if n <= 1: return False
  if n == 2: return True

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True


def main():
  n = int(input())

  for i in range(1,n):
    if i == 1:
      continue
    x = i
    y = n - i
    if not is_prime(x) and not is_prime(y):
      print(x,y)
      break

    

if __name__ == "__main__":
  main()  