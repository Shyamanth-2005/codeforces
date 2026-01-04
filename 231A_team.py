# n problems
# they will attend a problem if atleast 2 out of 3 are sure of the solution
# else they won't solve the problem 


def main():
  n = int(input())
  problem_solved = 0
  while n > 0:
    problem = list(map(int,input().split()))
    if sum(problem) >= 2:
      problem_solved += 1
    n -=1
  return problem_solved

if __name__ == "__main__":
  res = main()
  print(res)