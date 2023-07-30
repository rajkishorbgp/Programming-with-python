'''
                        Program: 9
    Write a program to dispaly *'s in Right angled triangled form.

'''
'''
    A right-angled triangle is a triangle, that has one of its interior angles equal 
    to 90 degrees or any one angle is a right angle. Therefore, this triangle is also 
    called the right triangle or 90-degree triangle. The right triangle plays an important 
    role in trigonometry. Let us learn more about this triangle in this article. 

                              *
                            * *
                          * * *
                        * * * *
                      * * * * *

'''
n = 6

k = n
for i in range(1, n):
    print("  "*(k-i), end='')
    print('* '*i)

'''
Output:
          * 
        * *
      * * *
    * * * *
  * * * * *

'''
