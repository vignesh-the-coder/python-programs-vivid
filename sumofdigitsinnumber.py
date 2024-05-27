number = int(input("Enter the number: "))
result = 0

#we can use this in while line for i in range (len(str(num))):
while number>0:
    digit = number % 10
    result += digit
    number = number // 10
print("the sum is: ",result)    