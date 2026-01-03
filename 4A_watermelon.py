# wieght of the watermelon 

# divide the watermelon into even weights but not nessary the same weight




def main():
  w = int(input())
  if w == 2:
    return "NO"
  if w %2 != 0:
    return "NO"
  return "YES"
if __name__ == "__main__":
  res = main()
  print(res)