student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    grade = ""
    score = student_scores[name]
    if score>=91 and score<=100:
        grade = "Outstanding"
    elif score>=81 and score<=90:
        grade = "Exceeds Expectations"
    elif score>=71 and score <=80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[name]=grade

# 🚨 Don't change the code below 👇
print(student_grades)





