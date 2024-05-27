#Your code below
r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
t=int(input())
s=[0]
l=[[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
    for j in range(c):
        l[i+1][j+1]=(m[i][j])
    l[i].append(0)
l.append([0 for i in range(c+2)])
l[-2].append(0)
for i in range(r+1):
    for j in range(c+1):
        if l[i][j]==t:
            s.append(l[i-1][j-1])
            s.append(l[i-1][j])
            s.append(l[i-1][j+1])
            s.append(l[i][j-1])
            s.append(l[i][j+1])
            s.append(l[i+1][j-1])
            s.append(l[i+1][j])
            s.append(l[i+1][j+1])
if len(s)==1:
    print("-1")
else:
    for i in s:
        if i!=0:
            print(i,end=" ")



# In Java
            
#    import java.util.*;
# public class Hello {

#     public static void main(String[] args) {
# 		Scanner sc = new Scanner(System.in);
# 		int r=sc.nextInt(),c=sc.nextInt();
# 		int arr[][] = new int[r][c];
# 		for(int i=0;i<r;i++) {
# 		    for(int j=0;j<c;j++) {
# 		        arr[i][j] = sc.nextInt();
# 		    }
# 		}
# 		int n = sc.nextInt(),x = -1,y = -1;
# 		for(int i=0;i<r;i++) {
# 		    for(int j=0;j<c;j++) {
# 		        if(arr[i][j]==n) {x=i;y=j;}
# 		    }
# 		} 
# 		if(x==-1) System.out.print(-1);
# 		else {
# 		    List<Integer> al = new ArrayList<>();
# 		    if(x-1>-1 && y-1>-1) al.add(arr[x-1][y-1]);
# 		    if(x-1>-1) al.add(arr[x-1][y]);
# 		    if(x-1>-1 && y+1<c) al.add(arr[x-1][y+1]);
# 		    if(y-1>-1) al.add(arr[x][y-1]);
# 		    if(y+1<c) al.add(arr[x][y+1]);
# 		    if(x+1<r && y-1>-1) al.add(arr[x+1][y-1]);
# 		    if(x+1<r) al.add(arr[x+1][y]);
# 		    if(x+1<r && y+1<c) al.add(arr[x+1][y+1]);
# 		    for(int t:al) System.out.print(t+" ");
# 		}
# 	}
# }         
