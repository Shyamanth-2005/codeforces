def main():
  a,b = list(map(int,input().split()))
  count = 0
  # limak triples after every year
  # bob double every year
  # a - limak inital weight
  # b - bob inital weight
  while a <= b:
    a *= 3
    b *= 2
    count += 1
  print(count)
    
if __name__ == "__main__":
  main()