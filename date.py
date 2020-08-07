import datetime

dt_now = datetime.datetime.now()
print(dt_now)

with open('test1.txt', 'a') as fw:
    fw.write( str(dt_now.year) + '/' + str(dt_now.month) + '/' + str(dt_now.day) + '\n')

