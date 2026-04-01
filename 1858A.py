def main():
  t  = int(input())

  for _ in range(t):
    a, b, c = list(map(int,input().split()))
   
    if a > b or (a == b and c % 2 == 1):
      print("First")
    else:
      print("Second")
  
if __name__ == "__main__":
  main()