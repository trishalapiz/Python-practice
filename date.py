year = 2020
month = 11
day = 5

str_year = str(year)
str_month = str(month)
str_day = str(day)

#standard = yyyy-mm-dd
#nz format = dd/mm/yyyy

if len(str_month) == 1 and len(str_day) == 1:
    str_month = "0" + str_month
    str_day = "0" + str_day
    print("Standard format: " + str_year + "-" + str_month + "-" + str_day)
    print("New Zealand format: "+ str_day + "-" + str_month + "-" + str_year)
elif len(str_day) == 1:
    str_day = "0" + str_day
    print("Standard format: " + str_year + "-" + str_month + "-" + str_day)
    print("New Zealand format: "+ str_day + "-" + str_month + "-" + str_year)
elif len(str_month) == 1: 
    str_month = "0" + str_month
    print("Standard format: " + str_year + "-" + str_month + "-" + str_day)
    print("New Zealand format: "+ str_day + "-" + str_month + "-" + str_year)
else:
    print("Standard format: " + str_year + "-" + str_month + "-" + str_day)
    print("New Zealand format: "+ str_day + "-" + str_month + "-" + str_year)
