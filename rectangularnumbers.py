n = int(input())
k = 2*n - 1

for i in range(k):
    for j in range(k):
        a = i if i<j else j
        a = a if a<k-i else k-i-1
        a = a if a<k-j else k-j-1
        print(n-a, end = '')
    print()

'''
    5
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
'''