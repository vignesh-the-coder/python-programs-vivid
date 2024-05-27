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
           