

# The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

# Boundary Condition(s): 3 <= N <= 100

# Input Format: The first line contains N.

# Output Format:

# The first N lines contain the desired pattern as shown in the Example Input/Output section.

# Example Input/Output 1:

# Input:

# 6

# Output
# 1 * * * * 2

# * 3 * * 4 *

# * * 5 6 * *

# * * 7  8 * *

# * 9 * * 10 *

# 11 * * * * 12


a=int(input())
b=1
c, d=0,a-1
for x in range(a):
    for y in range(a):
        if(y==c or y==d):
            print(b, end=" ")
            b+=1
        else:
            print("*",end=" ")
    c+=1
    d-=1
    print()
    
    

    #Or


# n=int(input())
# m,a=n+1,1
# for i in range(n//2):
#    print('* '*i,end='')
#    print(a,end='')
#    print(' *'*(n-2*i-2),end=' ')
#    print(a+1,end='')
#    print(' *'*i)
#    a+=2
# if n%2==1:
#    print('* '*(n//2),end='')
#    print(n,end='')
#    print(' *'*(n//2))
# for i in range(n//2-1,-1,-1):
#    print('* '*i,end='')
#    print(m,end='')
#    print(' *'*(n-2*i-2),end=' ')
#    print(m+1,end='')
#    print(' *'*i)
#    m+=2












    #java
#     import java.util.*;
# public class Hello {

#     public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int n = sc.nextInt(),t=0;
# 		for(int i=0;i<n;i++) {
# 		    for(int j=0;j<n;j++) {
# 		        if(i==j || i==n-j-1) {
# 		            System.out.print(++t +" ");
# 		        } else {
# 		            System.out.print("* ");
# 		        }
# 		    }
# 		    System.out.println();
# 		}
# 	}
# }