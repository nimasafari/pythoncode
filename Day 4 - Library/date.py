# import datetime
# from pytz import timezone

# eastern = timezone('Asia/Tehran')



# mydate = datetime.datetime.now(eastern)
# print(mydate)
# print(mydate.year)
# print(mydate.month)
# print(mydate.day)

####################################
# import jdatetime
# ff = jdatetime.datetime.now()
# print(ff)

####################################
# import datetime 
# # year, monthe, day
# f = datetime.datetime(2020, 5, 10)
# print(type(f))

####################################

import datetime

todaydate = datetime.datetime.now()
print(todaydate.strftime("%A"))
print(todaydate.strftime("%B"))
print(todaydate.strftime("%a"))
print(todaydate.strftime("%w")) # 0 - 6 <==== 2 : doshanbeh
print(todaydate.strftime("%d"))
print(todaydate.strftime("%b"))
print(todaydate.strftime("%m"))
print(todaydate.strftime("%H"))
print(todaydate.strftime("%I"))
print(todaydate.strftime("%M"))
print(todaydate.strftime("%p"))
print(todaydate.strftime("%S"))
print(todaydate.strftime("%f"))
print(todaydate.strftime("%c"))
print(todaydate.strftime("%u")) # 0 - 6 <==== 2 : doshanbeh


