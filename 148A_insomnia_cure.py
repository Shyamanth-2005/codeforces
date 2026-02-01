
def main():
  k,l,m,n,d = [int(input()) for _ in range(5)]
  damaged = 0
  for i in range(1,d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
      damaged += 1
  print(damaged)

if __name__ == "__main__":
  main()
