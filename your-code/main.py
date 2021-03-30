#1. Import the NUMPY package under the name np.
import numpy as np
import sys

#2. Print the NUMPY version and the configuration.

print(np.version.version)
"""
The NumPy version is: "1.19.2"
"""


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(0,99,(2,3,5))
print("\n Array de aleatorios de 3x2x5 usando np.radom.randint \n", a)

a= np.random.rand(2,3,5)
print("\n Array de aleatorios de 3x2x5 usando np.random.randn \n", a)

a = np.random.randn(2,3,5)

#4. Print a.

print("\n Array de aleatorios de 3x2x5 usando np.random.randn \n", a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print("\nMatriz de unos 3x2x5\n", b)


#7. Do a and b have the same size? How do you prove that in Python code?

if a.shape == b.shape:
        print(f"\nEl array a y b son iguales\n")
else:
        print("\nLos arrays no son iguales\n")

#8. Are you able to add a and b? Why or why not?
try:
        c = a + b
        print("Si es posible sumarlos saldría este mensaje.\n El resultado es:\n\n",c)

except Exception as e:
        print("La suma no es posible\n")
        print("Ha ocurrido un error: ",e.__class__)
        print(a.shape," es distinto a ", b.shape)
         

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

c_ = b.reshape(2,3,5)  #podíaos haberlo hecho con un reshape

c=np.transpose(b, (1, 2,0))

try:
        print(f"\nEl array a y c ahora son de iguales dimensiones\n")
        d = a + c
        print("Si es posible sumarlos saldría este mensaje.\n El resultado de:\n\n", a, ' +\n ', c," =\n ",d)
        print(a.shape," es igual a ", c.shape)
except Exception as e:
        print("La suma no es posible\n")
        print("Ha ocurrido un error: ",e.__class__)
        print(a.shape," es distiºnto a ", c.shape)




#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.




#12. Multiply a and c. Assign the result to e.

e = a * c
#13. Does e equal to a? Why or why not?
if (e == a).all() :
        print(f"\nLas matricies  'e' y 'a' son iguales porque multiplico elemento a elemento y una de ellas es la matriz 'todo unos'\n")
else:
        print(f"\nNo son iguales\n")



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=d.max()
d_min=d.min()
d_mean=d.mean()
print("\nEl valor máximo es :", d_max)
print("\nEl valor mínimo es :", d_min)
print("\nLa media es :", d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f=np.empty(d.shape)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller 
# than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

f[(d> d_min) &  (d < d_mean)]=25
f[(d > d_mean) & (d < d_max)]=75
f[d == d_mean]=50
f[d == d_min]=0
f[d == d_max]=100


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print("El array 'd' es:\n")
print(d)
print("\nEl array 'f' es:\n")
print(f)


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.


"""
print(d.shape)
#f_bonus= [[["X" for _ in range(d.shape[0])] for _ in range(d.shape(1)] for _ in range(d.shape(2))]
def escala_letras(x, d_min, d_max, d_mean):
        if x > d_min and x < d_mean:
                return 'A'            

        elif x > d_mean and x < d_max:
                return 'B'

        elif x == d_mean:
                return 'C'

        elif x == d_min:
                return 'D'

        elif x == d_max:
                return 'E'

        return 'CACA'
        
f_bonus=np.array([[[escala_letras(d[i,j,k], d_min, d_max, d_mean) for i in range(d.shape[0])] for j in range(d.shape[1]) ] for k in range(d.shape[2]) ])
print(f_bonus)


print("El array 'd' es:\n")
print(d)
print("\nEl array 'f_bonus' es:\n")
print(f_bonus)
