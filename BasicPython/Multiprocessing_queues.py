from multiprocessing import Process, Queue
import time

def f(input_q, output_q):
    while True:
        x = input_q.get()
        if x == 'exit':
            return
        time.sleep(0.1*(10-x))
        print(x)
        output_q.put(x**2)

if __name__ == '__main__':
    input_q = Queue()
    output_q = Queue()

    for x in [1, 2, 3, 4, 5, 6, 7, 8]:
        input_q.put(x)

    processes = [Process(target=f, args=(input_q, output_q)) for _ in range(4)]

    for p in processes:
        p.start()

    while True:
        if output_q.qsize() == 8:
            for _ in range(4):
                input_q.put('exit')
            break

    while not output_q.empty():
        print('Result:', output_q.get())

    for p in processes:
        p.join()

'''
The queues example demonstrates the use of queues in interprocess communication in Python, specifically in a scenario where you have more tasks than worker processes.

In this example, two `Queue` objects are created: `input_q` and `output_q`. The `input_q` is filled with numbers from 1 to 8, which represent the tasks to be processed.

Four worker processes are created, each executing the function `f`. This function continuously retrieves a number from `input_q`, sleeps for a duration inversely proportional to the number (0.1*(10-x) seconds), prints the number, and then puts the square of the number into `output_q`.

The worker processes are started, and the main process enters a loop where it continuously checks if `output_q` contains 8 elements. If it does, it puts the 'exit' command into `input_q` for each worker process and breaks the loop. This 'exit' command signals the worker processes to terminate.

Finally, the main process retrieves and prints the results (the squares of the numbers) from `output_q`.

This example demonstrates how queues can be used to distribute tasks among multiple worker processes and collect the results. It also shows how to gracefully terminate the worker processes by sending them an 'exit' command.
'''
