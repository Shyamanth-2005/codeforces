def main():
  n,k = list(map(int,input().split(" ")))
  scores = list(map(int,input().split(" ")))
  advanced  = 0
  k_score = scores[k-1]
  for score in scores:
    if score > 0 and score >= k_score:
      advanced +=1
  
  return advanced



if __name__ == "__main__":
  res = main()
  print(res)