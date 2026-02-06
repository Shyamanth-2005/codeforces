"""
n candies
a - alice
b - betty
a > b
a + b = n

a = b -n 

"""

def main():
  t = int(input())

  
  while t > 0:
    n = int(input())
    count = 0
    if n % 2 == 0:
      count = (n//2) - 1
    else:
      count = n // 2
    print(count)
    t -= 1






if __name__ == "__main__":
  main()