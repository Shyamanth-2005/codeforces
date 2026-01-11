def main():
  n  = int(input())
  lucky_count = 0

  while n > 0:
    last_digit = n % 10

      
      
    if last_digit == 4 or last_digit == 7:
      lucky_count += 1
    n //= 10
  
  if lucky_count ==  4 or lucky_count == 7:
    return "YES"
  return "NO"

if __name__ == "__main__":
  res = main()
  print(res)
    