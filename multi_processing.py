

import  multiprocessing
import time

def number_cube(n):
    time.sleep(2)
    print(f" cube is {n*n*n}")

def number_square(n):
    time.sleep(2)
    print(f"square is {n*n}")



p1 = multiprocessing.Process(target=number_cube, args=(5,))
p2 = multiprocessing.Process(target=number_square, args=(2,))

if __name__ =="__main__":
        p1.start()
        p2.start()

        p1.join()
        p2.join()
