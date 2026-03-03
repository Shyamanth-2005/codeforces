def parser(s: str) -> str:
  res = ''
  i = 0
  while i < len(s):
    if s[i] == '.':
      res += '0'
      i += 1
    else:
      if s[i + 1] == '.':
        res += '1'
      else:
        res += '2'
      i += 2
  return res


def main():
  s = input()
  res = parser(s)
  print(res)

if __name__ == "__main__":
  main()
