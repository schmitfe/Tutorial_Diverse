import socket
import multiprocessing
import time

# This is a very simple example of a server and client using sockets in Python.
# The server might get stuck if no client connects to it, so you might need to stop it manually.

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()

    port = 9999

    # Bind to the port
    server_socket.bind((host, port))

    print("Waiting for a connection...")
    # Queue up to 5 requests
    server_socket.listen(5)

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()

        print("Got a connection from %s" % str(addr))

        # Send a thank you message to the client.
        message = 'Thank you for connecting'+ "\r\n"
        client_socket.send(message.encode('ascii'))

        client_socket.close()

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()

    port = 9999

    # Connection to hostname on the port.
    client_socket.connect((host, port))

    # Receive no more than 1024 bytes
    message = client_socket.recv(1024)

    client_socket.close()

    print(message.decode('ascii'))

if __name__ == '__main__':
    # Start the server in a child process
    server_process = multiprocessing.Process(target=start_server)
    server_process.start()
    print("Waiting for server to start...")
    time.sleep(3)
    # Start the client in the main process
    start_client()

'''
This script demonstrates inter-process communication via sockets in Python. It includes a server process and a client process.

The server process is started in a child process using the multiprocessing module. It creates a socket, binds it to a specific address and port, and then listens for incoming connections. When a client connects, the server sends a message to the client and then closes the connection.

The client process runs in the main process. It creates a socket and connects to the server's address and port. It then receives a message from the server and prints it.

The server and client are running on the same machine for simplicity. In a real-world scenario, they could be on different machines. This concept is especially useful when using multiple Docker containers to run an application with multiple components. Each component can run in its own container and communicate with others via sockets, allowing for a modular and scalable architecture.

Here's a brief explanation of the code:

- The `start_server` function creates a server socket, binds it to the local machine name and a specific port, and listens for incoming connections. When a client connects, it sends a message to the client and then closes the connection.
- The `start_client` function creates a client socket, connects to the server's address and port, receives a message from the server, and prints it.
- In the main part of the script, a new process for the server is created and started using `multiprocessing.Process`. The client is started in the main process.
'''