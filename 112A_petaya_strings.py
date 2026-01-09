def main():
  string_1  = input().lower()
  string_2 = input().lower()
  if string_1 == string_2:
    return 0
  if string_1 > string_2:
    return 1
  if string_1 < string_2:
    return -1
    
  
if __name__  == "__main__":
  res = main()
  print(res)