
def main():
  m,n = list(map(int,input().split(" ")))
  total_squares = m * n
  return total_squares // 2

if __name__ == "__main__":
  res = main()
  print(res)