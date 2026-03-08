def main():
  t = int(input())

  while t > 0:
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    if k == 1:
      if arr == sorted(arr):
        print("YES")
      else:
        print("NO")
    else:
      print("YES")
    t -= 1

if __name__ == "__main__":
  main()