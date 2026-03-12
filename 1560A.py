def valid(n: int) -> bool:
  return n % 3 != 0 and n % 10 != 3

def main():
  seq = []
  i = 1
  while len(seq) < 1000:
    if valid(i):
      seq.append(i)
    i += 1
  

  t = int(input())

  for _ in range(t):
    k = int(input())

    print(seq[k - 1])

if __name__ == "__main__":
  main()



