# -*- coding: utf-8 -*-
#"""
#Created on Mon Oct 16 15:35:20 2023

#@author: dell
#"""
# first question 

a=float(input("a : "))
b=float(input("b : "))
c=float(input("c : "))
if a>b:
    if b>c:
        print("a,b,c")
    elif b<c:
        if a>c:
            print("a,c,b")
        elif a<c:
            print("c,a,b")
elif a<b:
    if b<c:
        print("c,b,a")
    elif b>c:
        if a>c:
            print("b,a,c")
        elif a<c:
            print("b,c,a")
        
        
#question 2.1

import numpy as np
M1 = np.random.randint(0, 51, size=(5, 10))
M2 = np.random.randint(0, 51, size=(10, 5))
print("M1:")
print(M1)
print("M2:")
print(M2)


#question 2.2
#I got inspired by reading
#https://wenku.csdn.net/answer/de84e63cb56d41d08ac01b3c460dc782
    
import numpy as np
M1 = np.random.randint(0, 51, size=(5, 10))
M2 = np.random.randint(0, 51, size=(10, 5))

def matrix_multiplication(M1, M2):
    row_M1, col_M1 = len(M1), len(M1[0])
    row_M2, col_M2 = len(M2), len(M2[0])
    if col_M1 != row_M2:
        return None
    result = [[0 for _ in range(col_M2)] for _ in range(row_M1)]
    for i in range(row_M1):
        for j in range(col_M2):
            for k in range(col_M1):
                result[i][j] += M1[i][k] * M2[k][j]
    return result

result = matrix_multiplication(M1, M2)
if result is not None:
    for row in result:
        print(row)
else:
    print("矩阵无法相乘")



#question 3
#I got inspired by reading
#ways:https://www.mathsisfun.com/pascals-triangle.html
#https://blog.csdn.net/m0_62338174/article/details/129746943

def Pascal_triangle(k):
    row = np.zeros(k+1, dtype=float)
    row[0] = 1
    for i in range(1, k + 1):
        row[i] = row[i - 1] * (k - i + 1) /i 
    return row
print("Pascal triangle（k = 100) :")
print(Pascal_triangle(99))
print("Pascal triangle（k = 200) :")
print(Pascal_triangle(199))


#question 4

def Least_moves(x):
    steps = np.full(x + 1, 101)
    steps[1] = 0 
    for i in range(2, x + 1):
        if i % 2 == 0:
            steps[i] = steps[i // 2] + 1
        else:
            steps[i] = steps[i - 1] + 1
    print(int(steps[x]))
Least_moves(2)  
Least_moves(5) 

#question 5.1
#consult with my roommate he teach how to set up the function and caculate

def Find_expression(target, current_expr="", current_num=1):
    if current_num == 10:
        # 如果当前数字已经是9，检查当前表达式是否等于目标整数
        if eval(current_expr) == target:
            print(current_expr + " = " + str(target))
        return

    # 选择1：将当前数字添加到当前表达式并继续递归
    Find_expression(target, current_expr + str(current_num), current_num + 1)

    # 选择2：在当前表达式中添加加法运算符并继续递归
    Find_expression(target, current_expr + "+" + str(current_num), current_num + 1)

    # 选择3：在当前表达式中添加减法运算符并继续递归
    Find_expression(target, current_expr + "-" + str(current_num), current_num + 1)

# 测试函数，找到所有满足条件的表达式
Find_expression(50)

# question 5.2 l have no idear about this question
import matplotlib.pyplot as plt



