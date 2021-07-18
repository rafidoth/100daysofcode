scores = input("enter scores with space").split()

scores = list(map(int, scores))

print(scores)

high_score = 0

for n in scores:
  if n > high_score:
    high_score = n


print(high_score)

