# 1<n < 1000

def main():
  n,k,l,c,d,p,nl,np = list(map(int,input().split()))

  # to make a toast 
  # n - number of frinds = 3
  # k - no of bottles = 4
  # l - milliters of drink = 5
  # c - no of limes = 10
  # d - no of slices = 8
  # p - grams of salt = 100
  # cd - no of sliced limes 
  # nl - mililiters of drink = 3
  # np - grams of salt = 1


  # no of milliters = k * l = 20 // nl
  # no of slices  = c * d = 80 
  # no of  grams = p // np

 # min((k*l)//nl,c*d,p//np)//n 


  ans = min((k*l)//nl,c*d,p//np)//n
  print(ans)




if __name__ == "__main__":
  main()