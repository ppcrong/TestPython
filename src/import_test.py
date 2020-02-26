import time
import datetime as dt
import math

print(time.__name__)
print(dt.__name__)
print(dt.datetime.now())
print(math.__name__)

# startTime = time.time()
# print('start time:', startTime)
#
# time.sleep(3)
# for n in range(10):
#     print(n)
#
# print('end time:', time.time() - startTime)

print('time.time():', time.time())
print('time.timezone:', time.timezone)

print('Date:', dt.datetime.now().date())
print('Time:', dt.datetime.now().time())
