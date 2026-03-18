# ti = 1 good at programing
# ti = 2 good at maths
# ti = 3 good at PE
def procedure(n, t):
  if n < 3:
    print(0)
    return
  ones, twos, threes = [], [], []
  
  for idx, item in enumerate(t):
    if item == 1:
      ones.append(idx + 1)
    elif item == 2:
      twos.append(idx + 1)
    elif item == 3:
      threes.append(idx + 1)
  
  w = min(len(ones), len(twos), len(threes))
  
  print(w)
  
  for i in range(w):
  
    print(ones[i], twos[i], threes[i])
        
        
      
      
    
  
  
def main():
  n = int(input())
  t = list(map(int,input().split()))
  
  procedure(n, t)

if __name__ == "__main__":
  main()