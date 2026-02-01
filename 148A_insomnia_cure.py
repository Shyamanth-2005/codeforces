import sys
def main():
  k = int(input())
  l =int(input())
  m = int(input())
  n = int(input())
  d = int(input())
  dragons = [i for i in range(1,d+1)]
  for i in range(len(dragons)):
    if dragons[i] % k == 0:
      dragons[i] = 0
    if dragons[i] % l == 0:
      dragons[i] = 0
    if dragons[i] % m == 0:
      dragons[i] = 0
    if dragons[i] % n == 0:
      dragons[i] = 0
  print(dragons.count(0)) 
      

if __name__ == "__main__":
  main()
