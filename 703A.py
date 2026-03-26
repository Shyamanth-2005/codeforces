def main():
  chris_cnt = 0
  mishka_cnt = 0

  t = int(input())

  for _ in range(t):
    m, c = list(map(int,input().split()))
    if max(m, c ) == m:
      mishka_cnt += 1
    if max(m , c) == c:
      chris_cnt += 1
    
  if mishka_cnt > chris_cnt:
    print("Mishka")
  elif chris_cnt > mishka_cnt:
    print("Chris")
  else:
    print("Friendship is magic!^^")


if __name__ == "__main__":
  main()

    
