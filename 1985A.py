def swap(a: str, b: str) -> list[str]:
  temp_a = a
  temp_b = b
  a = b[0] + a[1:]
  b = temp_a[0] + temp_b[1:]
  return [a, b]
def main():
  t = int(input())

  for _ in range(t):
    a, b = list(map(str,input().split()))
    a, b = swap(a, b)

    print(a, b)

if __name__ == "__main__":
  main()
