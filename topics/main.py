# print("Hello world")
# class Node: 
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
# class LinkedList:
#     def __init__(self):
#         self.head = None

# if __name__ == "__main__":
#     pass

# factorial
def fact(num):
    temp = 1
    while num > 0:
        print("running for values: ", temp, num)
        temp = num * temp
        num = num - 1
    return temp

result = fact(5);
print(result)