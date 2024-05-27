# Given two integer variables a and b, and a boolean variable flag.
# The task is to check the status and return accordingly.
# Return True for the following cases:

# Either a or b (not both) is non-negative and flag is false.
# Both a and b are negative and flag is true.
# Otherwise, return false.

# Example: 

# Input:
# a = 1
# b = -1
# flag = False
# Output:
# True
# Explanation:
# Since a and b are positive and 
# negative respectively and flag
# is False, so return True.

#User function Template for python3

# Function to check value and 
# return accordingly
def check_status(a, b, flag):
    ##Your code here
    ##Either True or False is returned
    if (a > 0) ^ (b > 0) and flag == False:
        return True
    elif (a < 0) and (b < 0) and flag == True:
        return True
    else:
        return False
    

    