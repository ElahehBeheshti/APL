public class
MatrixMultiplication_Counting_Loops {
    public static void main(String[] args) {
        /*  Step 1: Check if the user has provided at least 6 arguments (4 for matrix sizes + matrix elements)
        Print a message to guide the user if the arguments are insufficient*/        
        System.out.println("Please provide matrix sizes and elements.");

        if (args.length < 6) {
            // Exit the program if the number of arguments is less than required
            return;
        }

        /*Step 2: Parse matrix sizes from the first four arguments
        Extract dimensions for Matrix A and Matrix B*/ 
        int rows_A = Integer.parseInt(args[0]); // rows of Matrix A
        int cols_A = Integer.parseInt(args[1]); // columns of Matrix A
        int rows_B = Integer.parseInt(args[2]); // rows of Matrix B
        int cols_B = Integer.parseInt(args[3]); // columns of Matrix B

        /*Step 3: Check if the matrices are compatible for multiplication
        Matrix multiplication requires cols_A of Matrix A to be equal to rows_B of Matrix B*/ 
        if (cols_A == rows_B) {
        // Initialize the result matrix for the product of A and B
        int[][] result = new int[rows_A][cols_B];
        // Proceed with the matrix multiplication...
        } else {
        // Print an error message if the matrices cannot be multiplied    
        System.out.println("Wrong input!!!!");
        return; // Terminate the program if the matrices are not compatible for multiplication
        }


        // Step 4: Calculate the number of matrix elements expected
        int expectedElementsA = rows_A * cols_A; // Total elements for Matrix A
        int expectedElementsB = rows_B * cols_B; // Total elements for Matrix B
       

        // Step 5: Initialize Matrix A and Matrix B
        // Create matrices with the specified dimensions
        int[][] matrixA = new int[rows_A][cols_A];
        int[][] matrixB = new int[rows_B][cols_B];
        int argIndex = 4; // Start reading matrix elements after the first 4 arguments (matrix sizes)
        
        // Fill Matrix A with the provided elements
        for (int i = 0; i < rows_A; i++) {
            for (int j = 0; j < cols_A; j++) {
                matrixA[i][j] = Integer.parseInt(args[argIndex++]);
            }
        }

        // Fill Matrix B with the provided elements
        for (int i = 0; i < rows_B; i++) {
            for (int j = 0; j < cols_B; j++) {
                matrixB[i][j] = Integer.parseInt(args[argIndex++]);
            }
        }

        // Step 6: Initialize the result matrix for the product of A and B
        int[][] result = new int[rows_A][cols_B];

        /*Step 7: Perform matrix multiplication using counting loops (nested loops)
        Calculate the product of Matrix A and Matrix B and store it in the result matrix*/
        for (int i = 0; i < rows_A; i++) {
            for (int j = 0; j < cols_B; j++) {
                for (int k = 0; k < cols_A; k++) { // or rows_B, because cols_A == rows_B
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        /*Step 8: Print the result matrix
        Display the result matrix in a readable format*/

        for (int i = 0; i < rows_A; i++) {
            for (int j = 0; j < cols_B; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println(); 
        }
    }
}