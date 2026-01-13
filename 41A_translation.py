def main():
  s = input()
  t = input()
  if s[::-1] == t:
    return "YES"
  return "NO"



if __name__ == "__main__":
  res = main()
  print(res)

