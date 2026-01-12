def main():
  n = int(input())
  games = list(input())
  a_count = 0
  d_count = 0
  for game in games:
    if game == "A":
      a_count += 1
    else:
      d_count += 1
  if a_count == d_count:
    return "Friendship"
  if a_count > d_count:
    return "Anton"
  return "Danik"


if __name__ == "__main__":
  res = main()
  print(res)