def process(a, b, c):
  if a + b >= 10 or a + c >= 10 or b + c >= 10:
    return "YES"
  return "NO"

def main():
  t = int(input())

  while t > 0:
    a,b,c = list(map(int,input().split()))
    res = process(a,b,c)
    print(res)
    t -= 1
if __name__ == "__main__":
  main()
