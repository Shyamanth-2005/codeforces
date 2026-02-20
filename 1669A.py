def division_cat(n : int) -> str:
  if n >= 1900 :
    return "Division 1"
  elif n <= 1899 and n >= 1600 :
    return "Division 2"
  elif n <= 1599 and n >= 1400 :
    return "Division 3"
  else:
    return "Division 4"
def main():
  t  = int(input())

  while t > 0:
    n = int(input())
    res = division_cat(n)
    print(res)
    t -= 1



if __name__ == "__main__":
  main()
