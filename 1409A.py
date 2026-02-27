def process(a: int, b: int) -> int:
  return (abs(a - b) + 9 ) // 10
 

  
def main():

  # k : [1, 10]
  # actions:
  # a = a + k
  # a = a - k

  # procees get a to b with all the possible actions

  t = int(input())

  while t > 0:
    a,b = list(map(int,input().split()))

    res = process(a,b)
    print(res)

    t -= 1

  


if __name__ == "__main__":
  main()
