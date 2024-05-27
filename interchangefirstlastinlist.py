# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping 
	temp = newList[0]                 #var as index 0
	newList[0] = newList[size - 1]     #index 0 as index last
	newList[size - 1] = temp            #index last as var
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
