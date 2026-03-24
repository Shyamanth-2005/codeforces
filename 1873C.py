# score_1 = 
def main():
  cnt_1 = 0
  cnt_2 = 0
  cnt_3 = 0
  cnt_4 = 0
  cnt_5 = 0

  grid = [input().strip() for _ in range(10)]
 
  for i in range(10):
    for j in range(10):
      if grid[i][j] == "X":
        if (0 <=i <= 9  and (j == 0 or j == 9)) or ((i == 0 or i == 9) and 0 <= j <= 9):
          cnt_1 += 1
        if (1 <= i <= 8 and (j == 1 or j == 8)) or ((i == 1 or i == 8) and 1 <= j <= 8):
          cnt_2 += 1
        if (2 <= i <= 7 and (j == 2 or j == 7)) or ((i == 2 or i == 7) and 2 <= j <= 7):
          cnt_3 += 1
        if (3 <= i <= 6 and (j == 3 or j == 6)) or ((i == 3 or i == 6) and 3 <= j <= 6):
          cnt_4 += 1
        if (4 <= i <= 5 and (j == 4 or j == 5)) or ((i == 4 or i == 5) and 4 <= j <= 5):
          cnt_5 += 1
  
  score = cnt_1 * 1 + cnt_2 * 2 + cnt_3 * 3 + cnt_4 * 4 + cnt_5 * 5
  return score


  # for i in range(10):
  #   for j in range(10):


if __name__ == "__main__":
  t = int(input())
  for _ in range(t):

    res = main()
    print(res)