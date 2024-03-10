import socket
import threading
import json


HOST = socket.gethostbyname("localhost")
PORT = 8080


def print_massage(sck: socket.socket):
    while True:
        try:
            rec = sck.recv(1024)
            receive = json.loads(rec.decode())
            print(f'\r{receive["name"]}: {receive["message"]}')
        except Exception as e:
            print(type(e), e)
        print(">>> ", end="")


def client(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        name = input("Enter your name: ")
        receive = threading.Thread(
            target=print_massage,
            args=(sock,),
            daemon=True)
        receive.start()
        while True:
            msg = input(">>> ")
            if msg == "exit":
                break
            massage = {
                "name": name,
                "message": msg
            }
            msg_bites = json.dumps(massage).encode()
            sock.sendall(msg_bites)


if __name__ == "__main__":
    client(HOST, PORT)
