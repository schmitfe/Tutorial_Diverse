import time
import threading
import multiprocessing

# CPU-bound function
def cpu_bound(n):
    while n > 0:
        n -= 1

# Using threads
def use_threads():
    n = 10**8

    start = time.time()
    threads = []
    for _ in range(2):
        thread = threading.Thread(target=cpu_bound, args=(n,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end = time.time()

    print('Time taken with threads:', end - start)

# Using processes
def use_processes():
    n = 10**8

    start = time.time()
    processes = []
    for _ in range(2):
        process = multiprocessing.Process(target=cpu_bound, args=(n,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
    end = time.time()

    print('Time taken with processes:', end - start)

use_threads()
use_processes()

'''
Global Interpreter Lock (GIL)
The GIL is a mechanism used in CPython that allows only one thread to execute Python bytecodes at a 
time in a single process, even on a multi-core system. This can be demonstrated by creating a CPU-bound 
function and running it in different threads and processes

In this example, when using threads, due to the GIL, the threads are not truly run in parallel, 
so the total time taken is roughly the time taken for both tasks to run sequentially. However, 
when using processes, each process runs on a different CPU core, bypassing the GIL, so the tasks are truly run in 
parallel, and the total time taken is roughly the time taken for the longest task.  In conclusion, In this example, 
when using threads, due to the GIL, the threads are not truly run in parallel, so the total time taken is roughly the 
time taken for both tasks to run sequentially. However, when using processes, each process runs on a different CPU core, 
bypassing the GIL, so the tasks are truly run in parallel, and the total time taken is roughly the time taken for the 
longest task.  In conclusion, threads in Python are best used for I/O-bound tasks where you need to handle blocking 
operations such as network I/O or disk I/O, while processes are best used for CPU-bound tasks where you need to perform 
heavy computations and want to take advantage of multiple CPUs or cores.threads in Python are best used for I/O-bound 
tasks where you need to handle blocking operations such as network I/O or disk I/O, while processes are best used for 
CPU-bound tasks where you need to perform heavy computations and want to take advantage of multiple CPUs or cores.
'''

# Note:
'''
Despite the Global Interpreter Lock (GIL) in Python, which allows only one thread to execute Python bytecodes at a time, 
we might still see utilization of multiple cores when using libraries like NumPy or external simulation software. 
This is because these libraries are often written in languages like C or Fortran, which do not have a GIL. 
When a Python program calls a function in such a library, the GIL is released, allowing the function to run on multiple cores simultaneously. 
Once the function finishes and control returns to the Python program, the GIL is reacquired. 
This is why you might see utilization of multiple cores when using these libraries or software, even though Python itself is limited by the GIL.
'''
