# 1.
# =========================================================
#         MATRIX OPERATIONS MANAGEMENT SYSTEM
# =========================================================


# A data analysis company stores numerical information in matrix form.
# To help employees perform matrix-related operations efficiently,
# the company wants a menu-driven application.

# The application should allow the user to:

# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# The user must enter the number of rows, columns, and all matrix
# elements. The program should perform the selected operation and
# display the result.

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user chooses Exit.

#    1. Add Two Matrices
#    2. Subtract Two Matrices
#    3. Compare Two Matrices
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all elements of Matrix A and Matrix B from the user whenever
#    required.

# 4. Based on the user's choice:

#    Choice 1 - Add Two Matrices
#    --------------------------------
#    Add corresponding elements of both matrices and display
#    the resultant matrix.

# 5. Choice 2 - Subtract Two Matrices
#    --------------------------------
#    Subtract corresponding elements of Matrix B from Matrix A
#    and display the resultant matrix.

# 6. Choice 3 - Compare Two Matrices
#    --------------------------------
#    Check whether both matrices are equal.

#    Two matrices are considered equal if:
#    - They have the same dimensions.
#    - Corresponding elements are equal.

#    Display:
#    "Matrices are Equal"
#    or
#    "Matrices are Not Equal"

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Operations Management System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 1

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 5 6
# 7 8

# Result Matrix:
# 6 8
# 10 12

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 3

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 1 2
# 3 4

# Output:
# Matrices are Equal

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Operations Management System

# =========================================================





row1 = int(input("Enter Number of rows in first Matrix: "))
column1 = int(input("Enter Number of column in first Matrix: "))
matrix1 = []
for i in range(row1):
    rows1 = []
    for j in range(column1):
        rows1.append(int(input("Enter The Element: ")))
    matrix1.append(rows1)




row2 = int(input("Enter Number of rows in second Matrix: "))
column2 = int(input("Enter Number of rows in second Matrix: "))
matrix2 = []
for i in range(row2):
    rows2 = []
    for j in range(column2):
        rows2.append(int(input("Enter The Element: ")))
    matrix2.append(rows2)


print("Matrix A")
for i in matrix1:
    for j in i:
        print(j,end=" ")
    print()

print("Matrix B")
for i in matrix2:
    for j in i:
        print(j,end=" ")
    print()








if row1 == row2 and column1 == column2:
    resultmatrix = []
    while True:
        print('''=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================''')

        print(''' Menu
         1. Add Two Matrices
         2. Subtract Two Matrices
         3. Compare Two Matrices
         4. Exit''')
        resultmatrix = []


        choise = int(input("Choose What do you want: "))
        match choise:
                case 1:
                    for i in range(len(matrix1)):
                        resultrow = []
                        for k in range(len(matrix1[i])):
                            resultrow.append(matrix1[i][k] + matrix2[i][k])
                        resultmatrix.append(resultrow)
                    for i in resultmatrix:
                        for j in i:
                            print(j,end=" ")
                        print() 



                case 2:
                    for i in range(len(matrix1)):
                        resultrow = []
                        for k in range(len(matrix1[i])):
                            resultrow.append(matrix1[i][k] - matrix2[i][k])
                        resultmatrix.append(resultrow)
                    for i in resultmatrix:
                        for j in i:
                            print(j,end=" ")
                        print()   

                case 3:
                    equal = []
                    for i in range(len(matrix1)):
                        for k in range(len(matrix1[i])):
                            if matrix1[i][k] == matrix2[i][k]:
                                equal.append(1)
                                break
                            else:
                                equal.append(0)

                    if 0 in equal:
                        print("Not Equal")
                    else:
                        print("Equal")
                            
                case 4:
                    break
else:
    print("Length are not Equal")






# 2.

# =========================================================
#             MATRIX ANALYSIS SYSTEM
# =========================================================


# A research laboratory stores experimental data in matrix form.
# Scientists want a program that can analyze the matrix and provide
# different statistics through a menu-driven application.

# The application should allow the user to:

# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Prime Numbers Row-wise
#    2. Count Perfect Numbers Column-wise
#    3. Display Row-wise Sum
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Prime Numbers Row-wise
#    ---------------------------------------
#    Count and display the number of prime numbers present
#    in each row of the matrix.

# 5. Choice 2 - Count Perfect Numbers Column-wise
#    --------------------------------------------
#    Count and display the number of perfect numbers present
#    in each column of the matrix.

#    Note:
#    A perfect number is a number that is equal to the sum
#    of its proper divisors.

#    Examples:
#    6  = 1 + 2 + 3
#    28 = 1 + 2 + 4 + 7 + 14

# 6. Choice 3 - Display Row-wise Sum
#    --------------------------------
#    Calculate and display the sum of each row.

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 2 4 5
# 6 7 8
# 11 28 13

# Output:
# Row 1 Prime Count = 2
# Row 2 Prime Count = 1
# Row 3 Prime Count = 2

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 2

# Output:
# Column 1 Perfect Number Count = 1
# Column 2 Perfect Number Count = 1
# Column 3 Perfect Number Count = 0

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 3

# Output:
# Row 1 Sum = 11
# Row 2 Sum = 21
# Row 3 Sum = 52

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Analysis System

# =========================================================




row= int(input("Enter Number of rows in first Matrix: "))
column= int(input("Enter Number of column in first Matrix: "))
matrix= []
for i in range(row):
    rows1 = []
    for j in range(column):
        rows1.append(int(input("Enter The Element: ")))
    matrix.append(rows1)


print("Matrix A")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()


while True:
    print('''=========================================================
                 MATRIX ANALYSIS SYSTEM
=========================================================''')

    print(''' Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit
''')
    resultmatrix = []

    choise = int(input("Choose What do you want: "))

    match choise:
        case 1:
            prime = []
            for row in matrix:
                count = 0
                for j in row:
                    if j > 1:
                        for k in range(2, j):
                            if j % k == 0:
                                break
                        else:
                            count += 1
                prime.append(count)

            for d in range(len(prime)):
                print(f"Row {d+1} Prime Count: {prime[d]}")  
        case 2:
            perfect = []
            for i in range(column):
                count= 0
                for j in range(row):
                    sum = 0
                    for k in range(i,matrix[j][i]):
                        print(matrix[j][i])
                        if matrix[j][i]%2==0:
                            sum += k
                if sum == matrix[j][i]:
                    count+=1
            perfect.append(count)

            print(perfect)           

        case 3:
            allsum = []
            for i in matrix:
                sum = 0 
                for j in i:
                    sum+=j
                allsum.append(sum)
            for k in range(len(allsum)):
                print(f"Row {k+1} Sum: {allsum[k]}")

        case 4:
            break



        



# 3.

# =========================================================
#          MATRIX QUALITY CHECK SYSTEM
# =========================================================

# Scenario

# A manufacturing company records quality inspection values in
# matrix form. The Quality Control team wants a menu-driven
# application to analyze the inspection data and generate reports.

# The application should allow the user to:

# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Armstrong Numbers Row-wise
#    2. Count Palindrome Numbers Column-wise
#    3. Display Average of Each Row
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Armstrong Numbers Row-wise
#    -------------------------------------------
#    Count and display the number of Armstrong numbers
#    present in each row.

#    Examples:
#    153, 370, 371, 407

# 5. Choice 2 - Count Palindrome Numbers Column-wise
#    -----------------------------------------------
#    Count and display the number of palindrome numbers
#    present in each column.

#    Examples:
#    121, 131, 444, 1221

# 6. Choice 3 - Display Average of Each Row
#    --------------------------------------
#    Calculate and display the average of each row.

# 7. Choice 4 - Exit
#    --------------------------------------
#    Display:
#    "Thank You for Using Matrix Quality Check System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 153 121 10
# 370 22 44
# 407 15 131

# Output:
# Row 1 Armstrong Count = 1
# Row 2 Armstrong Count = 1
# Row 3 Armstrong Count = 1

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Column 1 Palindrome Count = 0
# Column 2 Palindrome Count = 3
# Column 3 Palindrome Count = 2

# =========================================================








row= int(input("Enter Number of rows in first Matrix: "))
column= int(input("Enter Number of column in first Matrix: "))
matrix= []
for i in range(row):
    rows1 = []
    for j in range(column):
        rows1.append(int(input("Enter The Element: ")))
    matrix.append(rows1)


print("Matrix A")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()


while True:
    print('''=========================================================
              MATRIX QUALITY CHECK SYSTEM
=========================================================''')

    print(''' Menu
 1. Count Armstrong Numbers Row-wise
 2. Count Palindrome Numbers Column-wise
 3. Display Average of Each Row
 4. Exit
''')

    choise = int(input("Choose What do you want: "))

    match choise:
        case 1:
            armstrong = []
            for i in matrix:
                count = 0
                for j in i:
                    num1 = j
                    sum = 0
                    n = len(str(j))
                    sum= 0 
                    while j > 0:
                        num = j % 10
                        sum += num**n
                        j = j//10
                    if sum == num1:
                        count+=1
                armstrong.append(count)
            print(armstrong)
            for k in range(len(armstrong)):
                print(f"Row {k} Armstrong Count {armstrong[k]}")


        case 2:
            plindrome = []
            for i in range(len(matrix)):
                count  = 0
                for j in range(len(matrix[i])):
                    num = matrix[j][i]
                    if str(matrix[j][i]) == str(num)[::-1]:
                        count+=1
                plindrome.append(count)
            print(plindrome)
            for k in range(len(plindrome)):
                print(f"Column {k} Palindrome Count {plindrome[k]}")

        case 3:
            average = []
            for i in matrix:
                sum = 0
                for j in i:
                    sum += j
                average.append(sum/len(str(j)))
            for k in range(len(average)):
                print(f"Row {k} Average is {average[k]}")

        case 4:
            break





# 4.

# =========================================================
#         MATRIX DIAGONAL ANALYSIS SYSTEM
# =========================================================

# Scenario

# A security company stores surveillance data in matrix form.
# The analyst wants a menu-driven application to examine the
# diagonal elements of the matrix and generate reports.

# The application should allow the user to:

# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Display Main Diagonal Elements
#    2. Display Secondary Diagonal Elements
#    3. Compare Main and Secondary Diagonal Sums
#    4. Exit

# 2. Read the size of a square matrix from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Display Main Diagonal Elements
#    -----------------------------------------
#    Display all elements present in the main diagonal.

# 5. Choice 2 - Display Secondary Diagonal Elements
#    ----------------------------------------------
#    Display all elements present in the secondary diagonal.

# 6. Choice 3 - Compare Main and Secondary Diagonal Sums
#    ---------------------------------------------------
#    Calculate the sum of both diagonals and display:

#    - Main Diagonal Sum
#    - Secondary Diagonal Sum
#    - Which diagonal has the greater sum
#    - Or whether both sums are equal

# 7. Choice 4 - Exit
#    -----------------------------------------
#    Display:
#    "Thank You for Using Matrix Diagonal Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Enter size of matrix: 3

# Enter matrix elements:

# 1 2 3
# 4 5 6
# 7 8 9

# Menu
# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# Enter your choice: 1

# Output:
# Main Diagonal Elements:
# 1 5 9

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Secondary Diagonal Elements:
# 3 5 7

# ---------------------------------------------------------

# Enter your choice: 3

# Output:
# Main Diagonal Sum = 15
# Secondary Diagonal Sum = 15
# Both Diagonal Sums are Equal

# =========================================================


# 5.



row= int(input("Enter Number of rows in first Matrix: "))
column= int(input("Enter Number of column in first Matrix: "))
matrix= []
for i in range(row):
    rows1 = []
    for j in range(column):
        rows1.append(int(input("Enter The Element: ")))
    matrix.append(rows1)


print("Matrix A")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()


while True:
    print('''=========================================================
              MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================''')

    print(''' Menu
 1. Display Main Diagonal Elements
 2. Display Secondary Diagonal Elements
 3. Compare Main and Secondary Diagonal Sums
 4. Exit

''')

    choise = int(input("Choose What do you want: "))

    match choise:
        case 1:
            sum = 0
            for i in range(row):
                for j in range(column):
                    if i == j:
                        sum+=matrix[i][j]
            print("Main Diagonal Elements: ",sum)



        case 2:
            sum1 = 0
            n = len(matrix[0])
            for i in range(row):
                for j in range(column):
                    if j == n-1:
                        sum1+=matrix[i][j]
                        n-=1
            print("Secondary Diagonal Sum: ",sum1)

        case 3:
            if sum==sum1:
                print("Both the diagonal is equal")


        case 4:
            break





