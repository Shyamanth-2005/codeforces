def func(n):
  odd_n = 0
  even_n = 0
  if n % 2 != 0:
    odd_n = (n//2) +1
    even_n = n//2
  else:
    odd_n = even_n = n//2
  
  odd_sum =  odd_n ** 2
  even_sum = even_n*(even_n+1)
  
  return even_sum - odd_sum

def main():
  n = int(input())
  res = func(n)
  print(res)
  


if __name__ == "__main__":
  main()