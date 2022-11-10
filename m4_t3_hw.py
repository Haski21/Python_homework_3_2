"""
Дана строкa. Необходимо посчитать количество вхождений каждого символа.
Пример:
In: Hello, Python1
Out: 
H: 1
e: 1
l: 2
o: 2
,: 1
P: 1
y: 1
t: 1
n: 1
1: 1
 : 1
"""
'''
У меня 2 решения
Первое не совсем работает, заменяет элементы, но цикл не меняет.
Как я понимаю, возможно потому что адрес не меняется

Второе сделал через алфавит
'''
# str_first = input('Enter string:')
# for var_1 in range(len(str_first)):
#         char = str_first[var_1]
#         counter = 0
#         for  var_2 in range(len(str_first)):
#                 if char == str_first[var_2]:
#                     counter += 1
#         #             str_first.pop(var_2)
#     else: break
#     print(char, ':', counter)
# str_first.replace(char,'')
    
str_first = input('Enter string:')
nums = []

for char in str_first:
    if char not in nums:
        nums.append(char)

for char in nums:
    counter = 0
    for char_2 in str_first:
        if char_2 == char:
            counter += 1
    print(char, ':', counter)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    