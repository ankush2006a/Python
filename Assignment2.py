'''Assignment 2 Task 1 '''

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

'''Assignment 2 Task 2 '''

total = 0
for number in range(1, 51):
    total += number
print("The sum of numbers from 1 to 50 is:", total)
