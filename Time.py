import time

def t_time():
    start_time = time.time()
    time.sleep(0.1)
    return (time.time() - start_time)

def clock():
    start_clock = time.clock()
    time.sleep(0.1)
    return (time.clock() - start_clock)

count_time = 0
count_clock = 0

for i in range(1,10):
    count_time += t_time()
    count_clock += clock()

print("time =",count_time)
print("clock =",count_clock)