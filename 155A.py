def main():
  n = int(input())
  contests = list(map(int,input().split()))

  min_score = max_score = contests[0]
  count = 0
  for score in contests[1:]:
    if score < min_score :
      min_score = min(min_score,score)
      count += 1
    if score > max_score:
      max_score = max(max_score,score)
      count += 1
  
  print(count)
      



if __name__ == "__main__":
  main()