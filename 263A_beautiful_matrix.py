def main():
  mat = [list(map(int,input().split(" "))) for i in range(5)]
  """
    0 1 2 3 4
  0 0 0 0 0 0
  1 0 0 0 0 1
  2 0 0 0 0 0
  3 0 0 0 0 0
  4 0 0 0 0 0
  
  [1][4]
  [2][2]
  i_dis = abs(cur_i_index - target_i_index)
  j_dis = abs(cur_j_index - target_j_index)
  total_dis = i_dis + j_dis
  find the minimum number of steps needed to move the 1
  from the random pos to [2][2]
  """
  current_row_index = 0
  current_col_index = 0
  target_row_index = 2
  target_col_index = 2
  for row in range(5):
    for col in range(5):
      if mat[row][col] == 1:
        current_row_index = row
        current_col_index = col
  
  row_wise_shift = abs(current_row_index - target_row_index)
  col_wise_shift = abs(current_col_index - target_col_index)
  min_num_moves = row_wise_shift + col_wise_shift
  return min_num_moves

if __name__ == "__main__":
  res = main()
  print(res)