    
'''7.1.you are given with a comma separated natural numbers 1 to 10 print even numbers''' 
'''7.2 how many even numbers are there'''
'''7.3 you are given with a space separated integer list find no of even elements and odd elements in a list '''
'''my_list=list(map(int,input().split(",")))
count=0
sum=0
for i in range(1,len(my_list),2):
        # print(my_list[i],end=" ") for even numbers op:2 4 6 8 10
    count+=1
print(count)'''
my_list=list(map(int,input().split(",")))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)