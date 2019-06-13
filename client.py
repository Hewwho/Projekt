from socket import *
from threading import *

s = socket(AF_INET, SOCK_STREAM)

try:
    # s.connect((gethostbyname(gethostname()), 6666))
    s.connect(("192.168.196.1", 6666))
except error:
    exit(1)


def from_server():
    while True:
        try:
            data = s.recv(1024).decode()
            print(data)

            if data == "EXIT":
                s.close()
                exit(0)
        except error:
            pass


Thread(target=from_server).start()

while True:
    try:
        s.send(input().encode())
    except OSError:
        exit(0)
