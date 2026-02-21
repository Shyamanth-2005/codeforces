# a + b , a + c , b + c , a + b + c

# 2 + 1 , 2 + 3 , 1 + 3 , 2 + 1 + 3

#  3    ,  5    ,   4 ,       6

def main():
  x = list(map(int,input().split()))
  ans = []
  # a + b + c
  max_num = max(x)
  for num in x:
    if num != max_num :
      ans.append(max_num - num)
  
  print(*ans)




if __name__ == "__main__":
  main()