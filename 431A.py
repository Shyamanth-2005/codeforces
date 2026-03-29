def main():
  a1, a2, a3, a4 = list(map(int, input().split()))
  s = input()
  calorie_map = {
    "1": a1,
    "2": a2,
    "3": a3,
    "4": a4
  }
  total_calorie = 0
  for num in s:
    calorie = calorie_map.get(num)
    total_calorie += calorie
  
  print(total_calorie)

if __name__ == "__main__":
  main()

  