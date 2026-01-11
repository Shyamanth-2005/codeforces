def main():
  string = input()
  upper_char = 0
  lower_char = 0
  for char in string:
    if char.isupper():
      upper_char += 1
    else:
      lower_char += 1
  
  if lower_char >= upper_char :
    return string.lower()
  return string.upper()

if __name__ == "__main__":
  res = main()
  print(res)