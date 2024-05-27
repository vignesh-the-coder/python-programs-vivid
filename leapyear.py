n = int(input("Enter the year you want to check? "))

if n % 4 == 0:
  if n % 100 == 0:
    if n % 400 == 0:
      print("The year is a leap year")
    else:
      print("The year is not a leap year")
  else:
    print("The year is a leap year")
else:
  print("The year is not a leap year")