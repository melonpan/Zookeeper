l, w, h = int(input()), int(input()), int(input())

# sum of lengths of all edges
length_sum = 4 * (l + w + h)

# surface area
surface_area = 2 * (l * w + w * h + l * h)

# volume
volume = l * w * h

print(length_sum)
print(surface_area)
print(volume)
