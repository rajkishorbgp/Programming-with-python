'''
                        Program: 10
    Write a program to display *'s in pyramid style(also known as equivalent triangle).

'''
n = 6

k = n
for i in range(1, n):
    print(" "*(k-i), end='')
    print('* '*i)

'''
Output:
     * 
    * *
   * * *
  * * * *
 * * * * *

'''
