"""
dmin  = |x2 - x1| + |x2 - x2| + |x3 - x2|
dmin = xmax - xmin
"""

def main():
  x = list(map(int,input().split()))
  print(max(x) - min(x))

if __name__ == "__main__":
  main()