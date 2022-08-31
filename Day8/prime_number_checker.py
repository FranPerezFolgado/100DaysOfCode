#Write your code below this line 👇
def prime_checker(number):
    if number == 1:
        print(f"{number} is not prime")
        return
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime")
            break
    else:
        print(f"{number}  is prime!")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
for i in range(1, 101):
    #n = int(input("Check this number: "))
    prime_checker(number=i)



