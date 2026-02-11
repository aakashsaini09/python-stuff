import random
# count positive numbers in array/list
nums = [1, -2, 3, -4, 5, -6, 7, -8, 9,  10]
positive_num_count = 0
for n in nums:
    if(n > 0):
        print(n, " is positive")
        positive_num_count = positive_num_count + 1
print("Total positive numbers: ", positive_num_count)



# sum of even numbers up to a given number n
num = int(input("Enter the number: "))
sum_even = 0
for i in range(1, num+1):
    if(i%2 == 0):
        sum_even = sum_even + i
print("Sum is: ", sum_even)


# print multiplication table for a given number upto 10, but skip 5th
for i in range(1, 11):
    if(i == 5):
        continue
    else:
        print(num, " x ", i, " = ", num * i)



# reverse a string using loop
inp_str = "nohtyp"
reversed_str = ""
for char in inp_str:
    reversed_str = char + reversed_str
print("revrersed string: ", reversed_str)


# factorial of a number
num = int(input("Enter your number: "))
factorial = 1
while num > 0:
    factorial = factorial * num
    num = num - 1

print(factorial)

# keep asking input until user guess the correct number (1-10)
sec_num = random.randint(1, 11)
while True:
    guess = int(input("Guess  the number between 1-10: "))
    if guess == sec_num:
        print("You win...")
        break
    elif guess > sec_num:
        print("Try smaller number")
    else:
        print("Try bigger number")
    