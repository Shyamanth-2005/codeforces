def way_long(string):
  if len(string) <= 10:
    return string
  modified_string = ""
  modified_string += string[0] + str(len(string[1:len(string)-1])) + string[-1]
  return modified_string
                                  
def main():
  n = int(input())
  while n > 0:
    string = input()
    res = way_long(string)
    print(res)
    n -= 1
  
if __name__ == "__main__":
  main()                      
