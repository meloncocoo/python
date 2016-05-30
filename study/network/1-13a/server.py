import socket
import sys
import argparse


HOST = 'localhost'
DATA_PAYLOAD = 2048
BACKLOG = 5


def echo_server(port):
    """ A simple a TCP server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (HOST, port)
    print("Starting up echo server on %s port %s" % server_address)

    try:
        sock.bind(server_address)
        # Listen to clients, backlog argument specifies the max no. of queued
        # connections
        sock.listen(BACKLOG)

        while True:
            try:
                print("Waiting to receive message from client")
                client, address = sock.accept()
                data = client.recv(DATA_PAYLOAD).decode()
                
                if data:
                    print("Data: %s" % data)
                    client.send(data.encode())
                    print("send %s bytes back to %s" % (data, address))
            except (KeyboardInterrupt, SystemExit):
                print("")
                raise Exception("Key board interrupt")
            
            client.close()

    except OSError as msg:
        print("Sock error: %s" % msg)
    except Exception as exc:
        print("Other error: %s" % str(exc))
    finally:
        print("Closing server on %s port %s" % server_address)
        # end connection
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Socket Server Example')
    parser.add_argument('--port', action = "store", dest = "port", type = int, required = True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
