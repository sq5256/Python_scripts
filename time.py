import time
time.sleep(1)

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.time())
abc = time.localtime()
print(time.mktime(abc))
