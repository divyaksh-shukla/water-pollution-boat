import datetime

starttime = datetime.datetime.now()
while(datetime.datetime.now() - starttime < datetime.timedelta(seconds=5)):
    print('', end='')
print('end')