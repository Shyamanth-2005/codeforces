def main():
  n, k = list(map(int,input().split()))
  y = list(map(int,input().split()))

  eligible_students = 0

  for i in y:
    if i <= 5 - k:
      eligible_students += 1
  
  print(int(eligible_students / 3))

if __name__ == "__main__":
  main()