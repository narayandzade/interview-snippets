
import threading
import time

def task1():
    print("Task 1 started", time.time())
    time.sleep(2)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task1)
t1.start()
t2.start()

t1.join()
t2.join()

print("Both tasks completed")
