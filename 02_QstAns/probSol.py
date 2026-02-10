import random
# Check age problem
age = int(input("Enter your age: "))
if (age <= 13):
    print("Child")
elif (age > 13 and age <= 18):
    print("Teenager")
elif (age > 18 and age <= 59):
    print("Adult")
else:
    print("Senior")



# Set price of ticket based of age and day (Discount on wed)
days = ["sun", "mon","tue", "wed", "thu", "fri", "sat"]
price = 12 if age >= 18 else 8
random_num = random.randint(0, 7)
if random_num == 3:
    price = price - 2
    print("Price is: ", price, " on ", days[random_num])
else:
    print("Price is: ", price, " on ", days[random_num])


# password strength check
paswrd = input("Enter your password: ")
if len(paswrd) < 6:
    print("Password is Weak")
elif len(paswrd) <= 10:
    print("Password is Medium")
else:
    print("Password is Strong")



# check if year is leap year (divisible by 4, but not by 100 unless also divisible by 400) 
year = int(input("Enter year: "))
if year % 4 == 0:
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("year is leap but divisible by 100 but also by 400")
        else: print("divisible by 4 but also with hundred and not by 400")
    else: print("year is leap (not divisible by 100)")
    # if(year % 100 == 0 and year % 400 == 0):
    #     print("Year is leap")
    # else: 
    #     print("divisible by 4 only")
else: 
    print("not a leap year")
if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Year is perfect leap year")
else:
    print("Year is not perfect leap year")