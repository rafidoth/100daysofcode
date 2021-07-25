student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    scores = student_scores[key]
    if scores > 90 and scores<=100:
        student_grades[key] = ["Outstanding"]
    elif scores > 80 and scores <= 90:
        student_grades[key] = ["Exceeds Expectations"]
    elif scores > 70 and scores <= 80:
        student_grades[key] = ["Acceptable"]
    elif scores <= 70 :
        student_grades[key] = ["Fail"]
                   
print(student_grades)





