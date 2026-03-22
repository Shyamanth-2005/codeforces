import math
def reduce (numerator, denominator):
  common_divisor  = math.gcd(numerator,denominator)

  reduced_numerator = numerator // common_divisor
  reduced_denominator = denominator // common_divisor
  
  return reduced_numerator, reduced_denominator



def main():
  y,w = list(map(int,input().split()))
  prob = 6 - max(y, w) + 1
  total = 6

  numerator, denominator = reduce(prob, total)

  print(f"{numerator}/{denominator}")
  


if __name__ == "__main__":
  main()
  


