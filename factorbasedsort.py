n=int(input())
a=list(map(int,input().split()))
b=[[len([1 for j in range(1,(i//2+1)) if i%j==0])+1,i] for i in a]
f=sorted(b,key=lambda x:x[0],reverse=True)
for i in f:
    print(i[1],end=' ')

# another way
    

#  def fact(a):
#     p=0
#     for i in range(1,int(a**0.5)+1):
#         if a%i==0:
#             p+=1
#     d=int(a**0.5)
#     if d**2==a:
#         return (p*2)-1
#     else:
#         return p*2
# a=int(input().strip())
# l=list(map(int,input().split()));p=[]
# for i in l:
#     p.append(fact(i))
# while len(p)>0:
#     u=p.index(max(p))
#     print(l[u],end=" ")
#     p.pop(u);l.pop(u)   
    



# IN          JAVA






# import java.util.*;
# public class Hello {
#     static int factor(int n){
#         int c=0;
#         for(int i=1;i<=n;i++){
#             if(n%i==0){
#                 c++;
#             }
#         }
#         return c;
#     }
#     public static void main(String[] args) {
# 		//Your Code Here
# 		Scanner sc=new Scanner(System.in);
# 		int n=sc.nextInt();
# 		int A[]=new int[n];
# 		int fact[]=new int[n];
# 		for(int i=0;i<n;i++){
# 		    A[i]=sc.nextInt();
# 		    fact[i]=factor(A[i]);
# 		}
# 		for(int i=0;i<A.length-1;i++){
# 		   for(int j=0;j<A.length-i-1;j++){
# 		       if(fact[j]<fact[j+1]||(fact[j]==fact[j+1]&&j>0&&A[j-1]==A[j+1])){
# 		           int t=fact[j];
# 		           fact[j]=fact[j+1];
# 		           fact[j+1]=t;
		           
# 		           int temp=A[j];
# 		           A[j]=A[j+1];
# 		           A[j+1]=temp;
# 		       }
# 		   }
# 		}
# 		for(int i=0;i<A.length;i++){
# 		    System.out.print(A[i]+" ");
# 		}
# }
# }