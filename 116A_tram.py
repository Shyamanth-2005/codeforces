# ai - exiting passengers
# bi - entering passengers
# at a stop ai gets out and bi gets in
# tram empty at first stop(a1=0) and last stop(bn=0)
# min cap such that it never exceeds the tram max cap
# first ai leaves only then bi enters
# n = no of stop and it starts from 1 to n

# so a1 = 0 and bn = 0
# j = 1 to i-1
# sum(bj) - sum(aj)


# max_cap = 
# 0 + 3 = 3
# 3 - 2 = 1 + 5 = 6
def main():
  n = int(input())
  max_cap = 0
  passenger_in_tram = 0
  
  while n > 0:
    ai,bi = list(map(int,input().split()))
    passenger_in_tram -= ai
    passenger_in_tram += bi
    max_cap = max(max_cap,passenger_in_tram)
    n -= 1
  print(max_cap)  


if __name__ == "__main__":
  main()