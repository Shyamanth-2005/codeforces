# actions
# 1 - place water in an empty cell 
# 2 -  remove water and place it in any other empty cell
# if i is empty and i - 1 and i + 1 is full then i is going to be filled
#  # this mean it is blocked
# . this means it is empty 
# no restriction on the use of action 2 
# blocked cells can neither contain water nor flip place water in them

def proc(water):
  
  if '.' not in water:
    return 0
  
  segs = water.split('#')
  
  for seg in segs:
    if len(seg) >= 3:
      return 2

  return water.count('.')
  
    
def main():
  t = int(input())
  
  for _ in range(t):
    n = int(input())
    water = input()
    
    res = proc(water)
    print(res)
  
  
if __name__ == "__main__":
  main()