
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