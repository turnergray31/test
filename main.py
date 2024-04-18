def rain(blocks):
    height = 0

    for i in range(1,len(blocks)-1):
      max_left = max(blocks[:i])
      max_right = max(blocks[i:])

      upper = min(max_left,max_right)

      height += max(0,upper-blocks[i])

    return height

print(rain([3,0,0,2,0,4]))
print(rain([0,1,0,2,1,0,1,3,2,1,2,1]))
print(rain([2,0,3,1,1,2,0,1]))
