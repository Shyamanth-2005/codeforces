def main():
  n = int(input())
  faces = 0
  polyhedrons = {
    "Tetrahedron" :4,
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron" : 12,
    "Icosahedron" : 20
  }

  while n > 0:
    poly = input()
    faces += polyhedrons[poly]
    n -= 1
  
  print(faces)

if __name__ == "__main__":
  main()