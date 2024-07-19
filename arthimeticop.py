'''

a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a**b)
print(a//b)


'''
'''age=int(input())
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>24 and age<45):
    print("two wheelers and four wheelers")
else:
    print("All") '''

'''apple=int(input())
bananas=int(input())
oranges=int(input())
total=700
sum=apple*15+bananas*12*4+oranges*5
if(sum<=total):
    print(" not cheated")
else:
    print(' cheated')
'''
''''
even and odd numbers
n=int(input())
if(n%2==0 and n>0):
    print("even positive number")
elif(n%2==0 and 0>n):
    print("even negative number")
elif(n%2!=0 and 0<n):
    print("odd positive number")
else:
    print("odd negative number")
'''


''' mr.z is selected for olympics,he is participating in swimming competition.Only one winner is selected in all the participants.mr.x and mr.y are frnds of z.
mr.x is participating in badmiton and mr.y in table tennis,according to the selection committee,the requirements for the badminton players are 140 cm height,
weight:factors of 2,body fat<12%.according to the selection committee,requirements of table tennis are
                                      height:min 118cm-148cm,weight:factors of no. of medals won by mr.z,bodyfat:14%
               according to the previous history z participated in 14 games out of which he is having success rate of 65%.Write a program 
     mr.x and mr.y and mr.z from india travel in a same plane or not?       '''  

height=int(input())
weight=int(input())
if(height==140 and weight%2==0):
    print 