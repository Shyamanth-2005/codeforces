def procedure(cards: str) -> str:
  if cards == "abc":
    return "YES"
  
  # 1 & 2 or 1 and 3 or 2 and 3
  x = ""
  x += cards[1] + cards[0] + cards[2]
    
  if x  == "abc":
    return "YES"
    
  y = ""
  y += cards[2] + cards[1] + cards[0]
    
  if y == "abc":
    return "YES"
  
  z = ""
  z += cards[0] + cards[2] + cards[1]
  
  if z == "abc":
    return "YES"

  return "NO"
  
  
  
def main():
  t = int(input())
  
  for _ in range(t):
    cards = input()
    res = procedure(cards)
    print(res)
    

if __name__ == "__main__":
  main()