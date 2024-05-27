str=input()
str1=""
list=str.split()
for i in range(len(list)):
    str1=""
    for j in range(len(list[i])-1,-1,-1):
        str1=str1+list[i][j]
    list[i]=str1
for i in list:
    print(i,end=" ")

'''
I am Simran
I ma narmiS
   ''' 