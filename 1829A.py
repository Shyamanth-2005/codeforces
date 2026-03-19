def procedure(s: str) -> int:
  check = 'codeforces'
  cnt = 0
  for i in range(10):
    if s[i] != check[i]:
      cnt+= 1
  return cnt

def main():
  t = int(input())

  for _ in range(t):
    s = input()
    res = procedure(s)
    print(res)

if __name__ == "__main__":
  main()
