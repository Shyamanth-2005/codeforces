def main():
  user_name = input()
  unique_char = set(user_name)
  if len(unique_char) % 2 == 1:
    print("IGNORE HIM!")
  else:
    print("CHAT WITH HER!")


if __name__ == "__main__":
  main()