def main():
  n = int(input())
  cards = list(map(int,input().split()))
  
  ans = [0,0]
  # ans[0] = sereja 
  # ans[1] = dima
  i , j  = 0 , n-1
  player_flag = 0
  while i <= j :
    
    if cards[i] > cards[j] :
      ans[player_flag] += cards[i]
      i += 1
    else:
      ans[player_flag] += cards[j]
      j -= 1
    
    if player_flag == 0 :
      player_flag = 1
    else:
      player_flag = 0

  print(*ans)



if __name__ == "__main__":
  main()