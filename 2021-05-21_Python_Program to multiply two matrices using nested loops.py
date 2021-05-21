#Program to multiply two matrices using nested loops
"Computer Programming Tutor_May 20,2021"

#3#3 Matrix A
a = [ [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
#3x3 Matrix B

b = [ [1,2,1],
      [2,4,6],
      [7,2,5]
    ]
#Results is also a 3x3 Matrix C
Matoutput = [ [0,0,0],
              [0,0,0],
              [0,0,0]
              ]
# Multiplying Matrix a by Matrix b
# Iteration through rows of Matrix a
for m in range(len(a)):
    #iteration through columns of Matrix b
    for n in range(len(b[0])):
        #Iteration through rows of Matrix b
        for k in range(len(b)):
            Matoutput[m][n] +=a[m][k]*b[k][n]
for z in Matoutput:
    print(z)
