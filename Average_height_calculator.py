heights = input("Enter heights with spaces").split()

for n in range(0, len(heights)):
  heights[n] = int(heights[n])

print(heights)

total_height=0
for a in heights:
  total_height += a

number_of_students = len(heights)

averageHeight = total_height/number_of_students
print(averageHeight)