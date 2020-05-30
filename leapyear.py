year = int(input('Leap year check! Please enter the year: '))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print (f"{year} is a leap year")
else:
    print (f'{year} is not a leap year')
