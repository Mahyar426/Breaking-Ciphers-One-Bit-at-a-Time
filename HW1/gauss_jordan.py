import numpy as np
import sys
def gauss(n , a):
    x = np.zeros(n)

    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(a[i][j])

    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

# Obtaining Solution

    for i in range(n):
        x[i] = a[i][n]/a[i][i]

# Displaying solution
    # print('\nRequired solution is: ')
    # for i in range(n):
    #     print('X%d = %0.2f' %(i,x[i]), end = '\t')

    return(x)
