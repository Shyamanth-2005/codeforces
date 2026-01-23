def main():
  n  = int(input())
  friends = list(map(int,input().split()))
  for i in range(n):
    print(friends.index(i+1) + 1,end=" ")
   

if __name__ =="__main__":
  main()