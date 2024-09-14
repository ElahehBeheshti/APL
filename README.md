# APL
Advanced Programming Language Assignments
Programming Assignment 1: Matrix Multiplication using Counting Loops

Objective:

The goal of this assignment is to help you understand the value of counting loops in programming. You will implement matrix multiplication using only counting loop constructs (i.e., for loops). This will reinforce your understanding of nested loops and matrix operations.

Assignment Details:

Language: Java
File Name: MatrixMultiplication_Counting_Loops.java
Class Name: MatrixMultiplication_Counting_Loops
Input: Accept matrix dimensions and elements from command-line arguments.
Output: Display the resultant matrix after multiplication.
Requirements:

Matrix Input:
You will read the matrix dimensions and elements from command-line arguments.
The matrices will be square (2X2) matrices (i.e., the same number of rows and columns), and their dimensions will be provided as the first argument.
Matrix elements should be read in row-major order.
Matrix Multiplication:
Implement matrix multiplication using counting loops (i.e., use nested for loops).
No use of any external libraries or in-built functions for matrix multiplication.
Output:
Print the resulting matrix to the console in a readable format.
Test Cases:

Input : java MatrixMultiplication_Counting_Loops 2 2 2 2 1 2 3 4 5 6 7 8
     Output: 19 22 43 50

Input : java MatrixMultiplication_Counting_Loops 2 2 2 2 -1 -2 3 4 5 -6 7 8
      Output: -19 -10 43 14

Input : java MatrixMultiplication_Counting_Loops 2 2 2 2 0 2 3 0 4 5 0 0
      Output: 0 0 12 15

Input : java MatrixMultiplication_Counting_Loops 1 2 3 4 5 6 7 8 9 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
      Output: Wrong input!!!!

Submission:

Submit your assignment by uploading the Java file named MatrixMultiplication_Counting_Loops.java to CodePost.
Ensure that your class name is MatrixMultiplication_Counting_Loops.
Grading Criteria:

Correctness: The program correctly multiplies the matrices and produces the expected output.
Use of Counting Loops: The matrix multiplication logic should strictly use for loops.
Code Style: The code should be well-organized, and variable names should be meaningful.
Command-Line Input Handling: The program should correctly handle and parse command-line arguments.
Total Points: 80 for the 4 test cases mentioned above. 