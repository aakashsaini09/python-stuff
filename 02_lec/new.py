# enumerate
x = ('Aakash', 'Aman', 'ankit', 'ajay')
# print(x)
y = enumerate(x)
print(y) # <enumerate object at 0x738d9e1ac810>
list(y)

# file manager
file = open('yt.txt', 'w')

try:
    file.write('This is the file for yt')
finally:
    file.close()
# or
with open('yt.txt', 'w') as file:
    file.write("This will also open file and doesn't need to close the file")
