#Program to solve a quadratic equation

import cmath

#Store the coefficients input from the user
a= float(input('Enter value of a:'))
b= float(input('Enter value of b:'))
c= float(input('Enter value of c:'))

print('The quadratic equation is: {0}x^2+{1}x+{2}=0'.format(a,b,c))

#Calculate determinant value
d= (b**2)-(4*a*c)

#Calcuate the roots of the eq.
x1= (-b+ (cmath.sqrt(d)) )/ 2*a
x2= (-b- (cmath.sqrt(d)) )/ 2*a

#Display the roots
print('Roots of the quadratic equation is {} & {}'.format(x1,x2))

