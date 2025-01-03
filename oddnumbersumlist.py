# In this example, we are using an if statement in a list comprehension with the condition that
# if the element of the list is odd then its digit sum will be stored else not.


# Explicit function 
def digitSum(n): 
	dsum = 0
	for ele in str(n): 
		dsum += int(ele) 
	return dsum 


# Initializing list 
List = [367, 111, 562, 945, 6726, 873] 

# Using the function on odd elements of the list 
newList = [digitSum(i) for i in List if i & 1] 

# Displaying new list 
print(newList) 


# Output :

# [16, 3, 18, 18]