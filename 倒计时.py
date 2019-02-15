import time
object_time = int(time.mktime(time.strptime("2019-03-05 00:00:00", "%Y-%m-%d %H:%M:%S")))
while True:
    remain_time = object_time - int(time.time())
    if remain_time == 0:
        break
    else:
        print("距离过年还有{}天{}小时{}分{}秒".format(int(remain_time/86400), int(remain_time%86400/3600),int(remain_time%3600/60),int(remain_time%60)))
        time.sleep(1)
print("2019年到了")