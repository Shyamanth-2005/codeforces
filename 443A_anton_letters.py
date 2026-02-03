def main():
  letters = input()
  char = set()
  for letter in letters:
    if letter.isalpha():
      char.add(letter)
    
  print(len(char))



if __name__ == "__main__":
  main()
