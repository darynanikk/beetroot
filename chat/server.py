import threading
import socket
import socketserver
from queue import Queue
from typing import List


HOST = socket.gethostbyname("localhost")
PORT = 8080
connections: List[socket.socket] = []
msgs_queue = Queue()


def response_all(clients: List[socket.socket], msg):
    while True:
        if msg.not_empty:
            data = msg.get()

            for con in clients:
                try:
                    con.sendall(data)
                except ConnectionError:
                    con.close()
                    clients.remove(con)
                    print(f"Connection with {con} closed")


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                data = self.request.recv(1024).strip()
                print(f"Received from {self.client_address[0]}")
            except Exception as e:
                print(type(e), e)
                break

            if not data:
                break

            msgs_queue.put(data)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def process_request(self, request, client_address):
        connections.append(request)
        print(f"Accepted connection from {client_address}")
        super().process_request(request, client_address)

    def server_close(self):
        for connection in connections:
            connection.close()
        super().server_close()


if __name__ == "__main__":
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    message_thread = threading.Thread(target=response_all, args=(connections, msgs_queue))
    message_thread.start()
    try:
        with server:
            ip, port = server.server_address
            print(f"Listening on {ip}:{port}")
            # Start a thread with the server -- that thread will then start one
            # more thread for each request
            server_thread = threading.Thread(target=server.serve_forever)
            # Exit the server thread when the main thread terminates
            server_thread.daemon = True
            server_thread.start()
            print("Server loop running in thread:", server_thread.name)
            server_thread.join()

    except KeyboardInterrupt:
        print("Closing the server.")
        server.server_close()
