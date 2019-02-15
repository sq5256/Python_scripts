import time,datetime
start_time = datetime.datetime.strptime("2018-01-01", "%Y-%m-%d")
delta_time = datetime.timedelta(days=1)
while True:
    print(str(start_time).split()[0])
    start_time = start_time + delta_time
    time.sleep(1)