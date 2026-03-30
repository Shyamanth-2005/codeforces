def main():
  

  t = int(input())

  for _ in range(t):
    points = 0

    n = int(input())
    s = input()

    seen = set()
    for char in s:
      if char not in seen:
        points += 2
        seen.add(char)
      else:
        points += 1
   
    
    print(points)
  
if __name__ == "__main__":
  main()


    
    