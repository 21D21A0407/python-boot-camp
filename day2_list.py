'''
my_list=[1,-2,2,0,9,3,4,-10,45,100,-100]
my_list=[1,2,3,4]
my_list.append(9999)#[1,2,3,4,9999]
my_list.insert(8000,999)
print(len(my_list))#4
my_list.pop(2) #[1 2 4]
my_list.pop(2000) #error
my_list_2=[5,6,7,8]
new_lst=my_list+my_list_2 # 1 2 3 4 5 6 7 8
new_lst=my_list.copy()
new_lst.pop()
print(*new_lst) #1 2 3
print(*my_list) #1 2 3 4
cnt=my_list.count(2)
print(cnt) #2
my_list.sort()
print(my_list)
'''
my_list=list(map(int,input().split(",")))
#my_list=list(map(int,input().split("@")))
choice=int(input("select any one of the choice\n1.append\n2.pop\n3.sort\n4.length"))
if(choice==1):
    my_list.append(100)
    print(*my_list)
elif(choice==2):
    my_list.pop(3)
    print(*my_list)
elif(choice==3):
    my_list.sort()
    print(*my_list)
else:
    print(f"Hello,the length of string is {len(my_list)}")