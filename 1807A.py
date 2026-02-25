def main():
  t =  int(input())

  while t > 0:

    a,b,c = list(map(int,input().split()))

    if a + b == c:
      print('+')
    else:
      print('-')

    t -= 1



if __name__ == "__main__":
  main()