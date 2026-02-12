def main():
  t = int(input())

  while t > 0:
    s = input().lower()

    if s == "yes":
      print("YES")
    else:
      print("NO")
    t -= 1


if __name__ == "__main__":
  main()