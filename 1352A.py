def main():
   t = int(input())

   while t > 0:
    n = list(map(int,(input())))
    rounds = []
    for i in range(len(n)):
      if n[i] != 0:
        rounds.append(n[i]* (10**(len(n)-i-1)))
    print(len(rounds))
    print(*rounds)

    t -= 1



if __name__ == "__main__":
  main()