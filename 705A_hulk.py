def main():
  n = int(input())

  ans = []


  for i in range(1,n):
    if i % 2 == 0:
      ans.append("I love that")
    else:
      ans.append("I hate that")
  res = " ".join(ans)
  if n % 2 == 1:
    res += " I hate it"
  else:
    res += " I love it"
  print(res)


if __name__ == "__main__":
  main()
