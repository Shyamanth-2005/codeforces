def sum_of_digits(n : str) -> int:
  n = int(n)
  _sum = 0
  while n > 0:
    last_digit = n % 10
    n //= 10
    _sum += last_digit
  
  return _sum

def main():
  t = int(input())

  while t > 0 :
    n = input()
    n1,n2 = n[:3],n[3:]
    _sum1 = sum_of_digits(n1)
    _sum2 = sum_of_digits(n2)

    print("YES" if _sum1 == _sum2 else "NO")

    t -= 1
  
if __name__ == "__main__":
  main()
