def function(n):
    print(n * n)
function(4)

arr_list = ["Aakash", "Aman", "Ankit", "Anshul", "Arnold", "Arjun", "Akshay", "Ajay"]
print(", ".join(arr_list))
print(len(arr_list))
print(arr_list[1:4])
arr_list_copy = arr_list.copy()
arr_list[4] = "Anurag"
print(arr_list)
print(arr_list_copy)
sqr_num = [n**2 for n in range(5)]
print(sqr_num)
for name in arr_list:
    print(name)

name = "Aakash"
for letter in name:
    print(letter)