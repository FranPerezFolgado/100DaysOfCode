# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum_heights = 0
count = 0
for height in student_heights:
    sum_heights += height
    count +=1

average1 = sum_heights / count
average =   sum(student_heights) / len(student_heights)
print(f"The average height is {average}")
#Write your code below this row 👇
