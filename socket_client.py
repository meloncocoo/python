from socket import *


HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)


def main():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = input('>')
        if not data:
            break
        client.send(data.encode())
        data = client.recv(BUFSIZE)
        if not data:
            break
        print(data.decode())

    client.close()

if __name__ == "__main__":
    main()
