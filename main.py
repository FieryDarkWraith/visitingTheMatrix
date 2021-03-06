from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 255 ]

#add_edge( matrix, 0, 250, 0, 500, 250, 0)
#add_edge( matrix, 250, 0, 0, 250, 500, 0)

print "\nEmpty Matrix\n"
emptyMatrix = new_matrix()
print_matrix(emptyMatrix)

print "\nTesting Identity Matrix\n" 
identMatrix = new_matrix()
#print_matrix( identMatrix )
ident( identMatrix )
print_matrix( identMatrix )

print "\nTesting Scalar Multiplication\n"
scalar_mult( identMatrix, 9 )
print_matrix( identMatrix )

print "\nCreating New Matrix and Adding Edge [10, 10, 0], [15, 15, 0]\n"
testMatrix = new_matrix( 0, 4)
add_edge( testMatrix, 10, 10, 0, 15, 15, 0)
print_matrix( testMatrix )

print "\nTesting Matrix Multiplication with Scalared Identity Matrix\n"
matrix_mult( identMatrix, testMatrix )
print_matrix( testMatrix )
#scalar_mult( matrix, 7 )

#matrix_mult( identMatrix, matrix )

#color = [ 255, 0 , 0]

#draw_lines( matrix, screen, color )

matrix = new_matrix( 0, 4)

for i in range(0, 500, 8):
    #add_edge( matrix, 0 + i, 0, 0, 500, 0 + i, 0)
    add_edge( matrix, 250, 0 + i/2, 0, 250 + i/2, 250, 0 )
    add_edge( matrix, 250, 0 + i/2, 0, 250 - i/2, 250, 0 )
    
    add_edge( matrix, 250 + i/2, 250, 0, 500, 250 + i/2, 0 )
    add_edge( matrix, 0, 500 - i / 2, 0, 0 + i / 2, 250, 0 )
#print_matrix(matrix) 

draw_lines( matrix, screen, color )

display(screen)
