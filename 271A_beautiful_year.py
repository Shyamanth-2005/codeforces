def main():
  y = int(input())
  out = y+1
  while len(set(str(out))) != 4:
    out += 1
  print(out)


if __name__ == "__main__":
  main()