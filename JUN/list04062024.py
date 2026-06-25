# 1. Count Pairs with Difference K

# A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

# Problem Statement:

# Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

# Example:

# Input:

# N = 5
# K = 2
# ages[] = {1, 5, 3, 4, 2}

# Output:

# 3

# Explanation:

# (1,3), (3,5), (2,4)

arr = []
n = int(input("Enter Number: "))
for i in range(n):
    num = int(input("Enter Element: "))
    arr.append(num)

num1 = int(input("Enter Which Difference You Find: "))

for i in range(len(arr)):
    for k in range(len(arr)):
        if i != k:
            if arr[i]-arr[k]==num1:
                print(f"{arr[i],arr[k]}",end=" ")



