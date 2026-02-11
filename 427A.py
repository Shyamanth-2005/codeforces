def main():
  n = int(input())
  events = list(map(int,input().split()))
  hired = 0
  crimes = 0
  for event in events:
    if hired == 0 and event == -1:
      crimes += 1
    elif event >= 1:
      hired += event
    elif hired != 0 and event == -1:
      hired -= 1  
  
  print(crimes)


if __name__ == "__main__":
  main()