# DAILY CHALLENGE

# ProgramID 5147

# SkillRack

# Next immediate Integer

# The program must accept an integer N as the input.
 #The program must print the next immediate integer that has all the digits in N as the output.
#If there is no such next immediate integer then the program must print -1 as the output.

# Boundary Condition(s): 1 <= N <= 10^6

# Input Format: The first line contains N.

# Output Format: The first line contains the next immediate integer that has all the digits in N or -1.

# Example Input/Output 1:

# Input 2586

# Output: 2658

# Explanation:

# The next immediate integer that has all the digits in 2586 is 2658. Hence the output is 2658

# Example Input/Output 2:

# Input

# 3111


# st=input().strip()
# li=[]
# for i in st:
#     li.append(int(i))
# n=len(li)
# idx=-1
# for i in range(n-2,-1,-1):
#     if li[i+1]>li[i]:
#         idx=i
#         break
# if idx!=-1:
#     for i in range(n-1,idx,-1):
#         if li[idx]<li[i]:
#             li[idx],li[i]=li[i],li[idx]
#             break
#     ki=li[:idx+1]+li[idx+1:][::-1]
#     st=""
#     for i in ki:
#         st=st+str(i)
#     print(st)
# else:
#     print("-1")




#Or

def f(n):
  d=sorted(list(str(n)))
  m=-1
  for i in range(n+1,10**6):
    if d==sorted(list(str(i))):
        m=i
        break
  return m
print(f(int(input())))





















#java





# import java.util.*;
# public class Hello {

#     public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		String s = sc.nextLine().trim();
# 		char c[] = s.trim().toCharArray();
# 		int i = c.length-2,j = c.length-1;
# 		while(i>=0 && c[i]>=c[i+1]) {
# 		    i--;
# 		}
# 		if(i==-1) {
# 		    System.out.print(-1);
# 		} else {
# 		    while(c[j]<=c[i]) {
# 		        j--;
# 		    }
# 		    char t = c[i];
# 		    c[i] = c[j];
# 		    c[j] = t;
# 		    Arrays.sort(c,i+1,c.length);
# 		    System.out.print(Integer.parseInt(new String(c)));
# 		}
# 	}
# }















