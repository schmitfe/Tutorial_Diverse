import threading
import multiprocessing

# Global variable
var = 0

def increment():
    global var
    var += 1

# Using threads
def use_threads():
    global var
    var = 0

    threads = []
    for _ in range(100):
        thread = threading.Thread(target=increment)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('Final value with threads:', var)

# Using processes
def use_processes():
    global var
    var = 0

    processes = []
    for _ in range(100):
        process = multiprocessing.Process(target=increment)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    print('Final value with processes:', var)

use_threads()
use_processes()

'''
Shared Memory Space
Processes in Python do not share memory space, while threads do. This can be demonstrated by creating a global 
variable and modifying it in a function that is run in different threads and processes.

In this example, when using threads, the var variable is shared among all threads, so its final value will be 100. 
However, when using processes, each process has its own memory space, so changes in one process do not affect others. 
Therefore, the final value of var will still be 0.
'''