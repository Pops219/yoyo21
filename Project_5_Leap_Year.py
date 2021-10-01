leap_year = int(input("Which year do you want to check? "))
if leap_year % 4 == 0:
    print(str(leap_year) + " is a leap year.")
elif leap_year % 100 == 0:
    print(str(leap_year) + " is a leap year.")
elif leap_year % 400 == 0:
    print(str(leap_year) + " is a leap year.")
else:
    print(str(leap_year) + " is not a leap year.")
