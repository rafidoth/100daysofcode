row1 = ["🎁", "🎁", "🎁"]
row2 = ["🎁", "🎁", "🎁"]
row3 = ["🎁", "🎁", "🎁"]

map = [row1, row2, row3] 
print(f"{row1}\n{row2}\n{row3}") 

position = input("Where do you want to move the X? (CR)")

horizontal = int(position[0]) -1
vertical = int(position[1]) -1

map[horizontal][vertical] = "X"

print(f"{row1}\n{row2}\n{row3}") 