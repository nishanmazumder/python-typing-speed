
# print("Hello Python!")

# IDENTIFIER
name = 'Nishan'
age = 28

# Data Type
rating = 5
is_true = True
complex_item = 5 + 6j

# Oprators
x = 10
y = 2

# print(x**2)

# input
# input1 = int(input('Enter number 1: '))  # int value
# input2 = int(input('Enter number 2: '))

# inputTotal = input1 * input2

# output
# print(inputTotal)

# Statement
# print('Please enter your age: ')

# num1 = int(input())

# if num1 > 18:
#     print('You can watch!')
# elif num1 == 18:
#         print('Not yet')
# else:
#     print('You cant watch!')

# RANGE
R = range(5, 10, 1)
R = list(R)
# print(R)

# Loop
n = 7
# while n<5:
#     print(n)
#     n+=1

# while n>=0:
#     print(n)
#     n-=1

# for x in range(10):
#     print(x*2, end=", ")

list_item = ['list1', 'list2', 'list3', 'list4', 'list5']

# for x in list_item:
#     print(x, end=", ")

list_number = range(10)

# for x in list_number:
#     if x==5:
#         continue
#     if x>7:
#         break
#     print(x)

# for x in list_item:
#     print(x)

# for i in range(len(list_item)):
#     print(list_item[i])

# [print (x) for x in list_item]

# new_list_item = []

# for x in list_item:
#     if "3" in x:
#         new_list_item.append(x)
#         print(new_list_item)

# print(list_number)

# String
fruit = "Apple"
paragraph = '''this is
multiline 
text'''
# print(fruit[2])

letter = "   abcde   "
# print(letter.upper().lstrip().rstrip()) # isupper(), islower(), isdigit(), isalpha(), upper(), lower(), lstrip(), rstrip()

# print(list_item)

# print(list_item[2:5:2])
list_item2 = ['book']
list_item[4] = "Apple"
list_item.append(letter)
list_item.extend(list_item2)

# print(list_item)

# list_item_range = [x for x in range(10)]
# less_range = [x for x in range(10) if x < 6]
# list_item_range = [3*x for x in range(10) if x%2 == 1]
# print(less_range)

# Function

# def sum_val(val1, val2):
#     c = val1 + val2
#     print(c)

# sum_val(4, 5)


# def greet_everyone(names):
#     for name in names:
#         print('hello', name)

# name_list = ['A', 'B', 'C', 'D']
# greet_everyone(name_list)

def greet_everyone(name_list):
    [print('Hello', x) for x in name_list]

name_list = ['A', 'B', 'C', 'D']

# greet_everyone(name_list)

# import math
# import math as m
# from math import *
# from math import pi
# print(math.pi)

# File
# data = open('data/data.txt', 'r')
    # print(data.read())
    # data.close()
    
with open('data/data.txt', 'w') as data:
    data.write('this is new line\n')
    data.writelines('test line')


