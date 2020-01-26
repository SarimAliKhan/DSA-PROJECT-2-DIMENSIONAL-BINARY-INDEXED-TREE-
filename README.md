# DSA-PROJECT-2-DIMENSIONAL-BINARY-INDEXED-TREE-
To change the matrix and queries of 2D BIT(Binary Indexed Tree) you just have to go inside the "Main()" function at the end of the py file. 
All the other functions in the class Matrix are not for user's work.They are only for executing the BIT,
Change the matrix in the "mat" variable on the first line of the function to your desired matrix which you want to give as a input(You can use numpy module for the array).
You have to keep this thing in your mind that the size/dimension you will give to the initiator of class Matrix(size) will be the exact size/dimension that your input matrix will have ,the size will be consisting of a single integer value given to the initiator of the class e.g Matrix(4) will create a matrix of 4*4.
Change the queries in the "coords" variable,keeping in my mind that 2D BIT works in bottom left to top right i.e(x1,y1,x2,y2).
You have to give coordinates using this information so that the BIT will work properly summing the values of sub matrix.
Lastly you will just have to initialize the class "Matrix(size)" in a variable and then call the function "Main(size)" using that variable.
