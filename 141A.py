def main():
  # print([1,2,3] == [2,1,3])
  # a = [1,2,3]
  # b = sorted([3,2,1])
  # print(a == b)
  guest = list(input())
  host = list(input())
  pile = list(input())
  final = guest + host
  final = sorted(final)
  pile = sorted(pile)
  
  print("YES" if final == pile else "NO")





if __name__== "__main__":
  main()