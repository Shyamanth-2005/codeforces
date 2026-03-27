def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def get_prime():
  return [i for i in range(2, 51) if is_prime(i)]

def main():
  prime_numbers = get_prime()
  n, m = list(map(int, input().split()))
  cur_idx = prime_numbers.index(n)
  if cur_idx < len(prime_numbers) - 1 and prime_numbers[cur_idx + 1] == m:
    return "YES"
  return "NO" 


  

if __name__ == "__main__":
  res = main()
  print(res)
