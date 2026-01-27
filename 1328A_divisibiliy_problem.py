def main():
  t = int(input())

  while  t > 0:
    a,b = list(map(int,input().split()))
    if a % b == 0:
      print(0)
      t -= 1
      continue
    q  = a // b
    mov = ((q+1) * b) - a 
    print(mov)
    t -= 1




if __name__ == "__main__":
  main()
