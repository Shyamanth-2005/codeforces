def codeforces_checker(c: str) -> str:
  main_str = "codeforces"

  if c in main_str:
    return "YES"
  
  return "NO"

def main():
  t = int(input())

  while t > 0:
    c = input()
    res = codeforces_checker(c)
    print(res)

    t -= 1
  
if __name__ == "__main__":
  main()