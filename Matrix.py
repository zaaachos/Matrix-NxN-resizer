
def function(matrix):                   # matrix should be a two-dimensional list like examples in README.md
     
     SixFour = [[1 for i in range(64)] for j in range(64)]      # 64 x 64 Matrix Initialization
     ThirtyTwo = [[1 for i in range(32)] for j in range(32)]         # 32 x 32 Matrix Initialization
     SixTeen = [[1 for i in range(16)] for j in range(16)]              # 16 x 16 Matrix Initialization
     Four = [[1 for i in range(4)] for j in range(4)]                 # 4 x 4 Matrix Initialization
     Two = [[1 for i in range(2)] for j in range(2)]            # 2 x 2 Matrix Initialization


     # check if given parameter is matrix.
     if not isinstance(matrix,list):
          print("Your given object, is not a matrix.")

     # check if given matrix has the same amount of columns and rows, like n x n and not n x y.
     if len(matrix) != len(matrix[0]):
          print("Your given matrix is not a n x n scalar. Matrix must be a square.")

     # check if the matrix given is n x n, and the n is factor of 64.
     if 64 % (len(matrix)) != 0:
          print("Your matrix cannot be resized. The number of rows and columns must be a factor of 64!")

     # boolean function to check if a given matrix contains ONLY int.
     def checktype(obj):
          for i in range(len(matrix)):
               for y in range(len(matrix[0])):
                    if not isinstance(matrix[i][y],int):
                         return False
          return True

     if not checktype(matrix):
          print("Your given matrix has some items, which are not Integers")


     capped = len(SixFour)//len(matrix)                # try to calculate the equivalent index of the given matrix for 64 x 64 matrix.
                                                       # to understand, watch the examples in the README.md

     """ Now we change our values and resize our n x n matrix into 64 x 64 matrix. """
     for x in range(len(SixFour)):
          for y in range(len(SixFour)):
               SixFour[x][y] = matrix[x//capped][y//capped]

     # print the result.
     for x in range(len(SixFour)):
               print(SixFour[x])




# example run for 4 x 4 into 64 x 64 matrix.
function([[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]])
