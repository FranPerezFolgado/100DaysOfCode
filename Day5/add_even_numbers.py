sum = 0
for n in range(1,101):
    if n % 2 == 0:
        sum+=n

print(f"The sum of the even numbers between 1 and 100 is {sum}")

sum = 0


for n in range(2, 101, 2):
    sum += n

print(f"The sum of the even numbers between 1 and 100 is {sum}")
