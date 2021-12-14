# # declarative style
# # 1
# list = [10, 20, 30, 40, 50]
# reversed_list = list[::-1]
# print(reversed_list)
# # 2
# nums = [10, 20, 30, 40, 50] 
# nums.reverse()
# print(nums)

# # imperative style
# # 1
# list = [10, 20, 30, 40, 50]
# reversed_list = []
# for i in range(len(list) - 1, - 1, -1):
#     reversed_list.append(list[i])
# print(reversed_list)
# # 2
# list = [10, 20, 30, 40, 50]
# reversed_list = []
# for num in list[::-1]:
#     reversed_list.append(num)
# print(reversed_list)



# list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# def myFilter(func, list, targetNumber):
#     filtered_nums = []
#     for num in list:
#         result = func(num, targetNumber)
#         if result:
#             filtered_nums.append(num)
#     return filtered_nums


# def less(num, target):
#     return num < target

# def greater(num, target):
#     return num > target

# print(myFilter(less, [10, 20, 30, 40, 50, 60, 70, 80, 90], 50))
# print(myFilter(greater, [10, 20, 30, 40, 50, 60, 70, 80, 90], 30))

# def calculator(func, a, b):
#     for num in a, b:
#         result = func(a, b)
#     return func(a, b)
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b
# print(calculator(add, 2, 3))
# print(calculator(subtract, 2, 3))
# print(calculator(multiply, 2, 3))
# print(calculator(divide, 2, 3))

# def sum_numbers(txt: str):
#     acc = 0
#     list = txt.split(' ')
#     for word in list:
#         if word.isdigit():
#             acc += int(word)
#     return acc
# print(sum_numbers('my numbers is 2'))
nums = [0, 1, 2, 3, 4, 5]
def checkio(list):
    acc = 0
    even_nums = nums[0::2]
    acc += even_nums
    last_num = nums.index[-1]
    return acc * last_num
print(checkio([0, 1, 2, 3, 4, 5]))

