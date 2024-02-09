from multiprocessing import Process, Lock
import time
def printer(item, lock):
    lock.acquire()
    try:
        print(item)
        time.sleep(0.5)
    finally:
        #pass
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    for item in items:
        Process(target=printer, args=(item, lock)).start()


'''
The lock example demonstrates the use of locks in interprocess communication in Python. 
In this example, a lock is created using the `Lock()` function from the `multiprocessing` module. 
This lock is then passed as an argument to multiple processes that are created.
The function `printer` is defined to print an item. Before it prints the item, it acquires 
the lock using `lock.acquire()`. This prevents other processes from executing the print statement at the same time. 
Once the item is printed, the lock is released using `lock.release()`, allowing other processes to acquire the lock 
and print their items.

The main part of the code creates a list of items and starts a new process for each item in the list. 
Each process executes the `printer` function with an item from the list and the lock as arguments. 

This ensures that even though multiple processes are started almost at the same time, the print statements are executed 
one at a time, in the order in which the processes were able to acquire the lock.
'''