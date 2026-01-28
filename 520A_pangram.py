def main():
  n = int(input())
  string  = input().lower()
  if n < 26:
    return "NO"
  
  seen = set()
  for letter in string:
    seen.add(letter)
  
  if len(seen) == 26:
    return "YES"
  return "NO"

if __name__ == "__main__":
  res = main()
  print(res)

  