n = int(input())
heights = list(map(int, input().split()))


max_height = max(heights)
max_index = heights.index(max_height)

min_height = min(heights)
min_index = -1
for i in range(n - 1, -1, -1):
    if heights[i] == min_height:
        min_index = i
        break


swaps = max_index + (n - 1 - min_index)


if max_index > min_index:
    swaps -= 1

print(swaps)
