import socket
import datetime
from time import ctime


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)


def testhostname():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("host name: %s (%s)", hostname, ip)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen(5)

    while True:
        print("Waiting for connection...")
        client, addr = s.accept()
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        print(time, " connected from: ", addr)

        while True:
            data = client.recv(BUFSIZE)
            if not data:
                break
            client.send(("[%s] %s" % (ctime(), data.decode())).encode())

    client.close()
    s.close()

if __name__ == '__main__':
    testhostname()
    main()
