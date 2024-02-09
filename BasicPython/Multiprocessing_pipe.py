from multiprocessing import Process, Pipe


def f(conn):
    conn.send(["hello world"])
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

"""
The pipe example demonstrates the use of pipes in interprocess communication in Python. 
In this example, a pipe is created using the `Pipe()` function from the `multiprocessing` module. 
This function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
The function `f` is defined to send a message through a connection. It takes a connection object as an argument, 
sends a list containing the string 'hello world' through the connection using `conn.send()`, and then closes the 
connection using `conn.close()`.
The main part of the code creates a parent and child connection using `Pipe()`, starts a new process that executes the `f` function with the child connection as an argument, receives the message from the parent connection using `parent_conn.recv()`, and then joins the process using `p.join()`.
Pipes and queues in Python's `multiprocessing` module are both used for interprocess communication, but they have some differences:

1. **Data Structure**: A pipe is a linear data structure that follows the FIFO (First In First Out) methodology, similar to a queue. However, a queue is a higher-level, thread and process-safe data structure that allows data to be safely pushed onto or popped off from multiple threads or processes.

2. **Communication**: Pipes are generally used for communication between two processes. The two ends of the pipe are used for sending and receiving data. On the other hand, queues can be used for communication between multiple processes. Data can be put into the queue from one end and retrieved from the other end.

3. **Usage**: Pipes are more primitive and require manual management of both ends of the pipe for sending and receiving data. Queues, being a higher-level structure, handle these details automatically and provide a simple interface with `put()` and `get()` methods for adding and retrieving data.

4. **Ordering**: Both pipes and queues maintain the order of the data. The first data sent into the pipe or queue will be the first one to come out.

In summary, while pipes can be used for simple, one-to-one communication between processes, queues are more suitable for complex scenarios where multiple processes need to exchange data in a thread-safe manner.
"""
