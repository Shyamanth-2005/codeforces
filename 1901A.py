def procedure(n: int, x: int, stations: list[int]) -> int:
  prev =  0
  mx_gap = 0

  for station in stations:
    mx_gap = max(mx_gap, station - prev)
    prev = station
  
  return max(mx_gap, 2 * (x - stations[-1]))


def main():
  t = int(input())

  for _ in range(t):
    n, x = list(map(int, input().split()))
    stations = list(map(int,input().split()))
    res = procedure(n, x, stations)
    print(res)
if __name__ == "__main__":
  main()
  
