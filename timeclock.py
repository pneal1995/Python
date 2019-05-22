import time
import timeit
import datetime


now = datetime.datetime.now()
print('Process started on', now)

start = time.time()
end = time.time()
print(end - start)

def my_function():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y

print(timeit.timeit(my_function, number=100000))