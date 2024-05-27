# 1 way
# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]    #returns the reverse string and checking it
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No") 

 #2 way

# def ispalindrome(str):
#     for i in range(0,int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
       
#     return True
# s = "malayalam"
# ans=ispalindrome(s)

# if ans:
#     print("yes")
# else:
#     print("no") 





   #3 way
    
    

# class Solution:
#     def sentencePalindrome(self, s):
#         #97, 122 indicates alphabets
#         # your code here
#         s.lower()
#         t = ''
        
#         x = [chr(i) for i in range(97,123)]
#         #print(x)
        
#         for ele in s:
#             if ele in x:
#                 t = t+ele
#         if t ==t[::-1]:
#             return(1)
#         else:
#             return(0)
                
