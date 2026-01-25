def main():
  b1 = list(map(int,list(input())))
  b2 = list(map(int,list(input())))
  for i in range(len(b1)):
    res =  b1[i] ^ b2[i]
    print(res,end="")
if __name__ == "__main__":
  main()