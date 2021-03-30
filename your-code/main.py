#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.array([
    [[55, 66, 3, 55, 67], [40, 90, 3, 98, 76], [23, 34, 55, 45, 55]],
    [[10, 10, 3, 78, 98], [10, 11, 3, 88, 33], [5, 55, 89, 78, 98]]
])


#4. Print a.
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5, 2, 3))



#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
a.size == b.size 
R: #TRUE



#8. Are you able to add a and b? Why or why not?
a + b
R: #FALSE, they have different shape!


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = np.transpose(b, axes=[1,2,0])


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = a + c
print(d)
R: It works because both have the same shape(2,3,5)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)
R: # The variable d is the sum of a and c. C is the transpose of b, it has the same numbers as b, but different shape(the shape is equal to a). Now, we have d that is the sum of a & the new c. The difference of both variables are 1, because we had to assign 1 to b.

#12. Multiply a and c. Assign the result to e.
e = a * c


#13. Does e equal to a? Why or why not?
(a == e).all()
#TRUE, because c is equal to 1.



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_mean = d.mean()
print(d_mean)
d_max=d.max()
print(d_max)
d_min=d.min()
print(d_min)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty(d.shape)



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
f1 = []

for n in np.nditer(d):
    if (n > d_min) and (n < d_mean):
        f1.append(25)
    elif (n > d_mean) and (n < d_max):
        f1.append(75)
    elif (n == d_mean):
        f1.append(50)
    elif (n == d_min):
        f1.append(0)
    else:
        f1.append(100)

f2 = np.array(f1)
f = f2.reshape((2,3,5))


print(f)



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
print(f)
print(d)
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
j=np.array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

f1 = []

for n in np.nditer(j):
    if (n > j_min) and (n < j_mean):
        f1.append("B")
    elif (n > j_mean) and (n < j_max):
        f1.append("D")
    elif (n == j_mean):
        f1.append("C")
    elif (n == j_min):
        f1.append("A")
    else:
        f1.append("E")
    

f2 = np.array(f1)
f = f2.reshape((2,3,5))


print(f)
##He cogido la misma d que ponia en el ejemplo (y le he llamado j) para que me resultara mas fácil ver las letras!!