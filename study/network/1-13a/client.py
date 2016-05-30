import socket
import sys
import argparse


HOST = 'localhost'

def echo_client(port):
    """ A simple echo client """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (HOST, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    # Send data
    try:
        # Send data
        message = "Test message. This will be echoed"
        print("Sending %s" % message)
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expectived = len(message)

        while amount_received < amount_expectived:
            data = sock.recv(16)
            amount_received += len(data)
            print("Received: %s" % data.decode())

    except OSError as msg:
        print("Socket error: %s" % msg)
    except Exception as exc:
        print("Other exception: %s" % exc.message)
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Socket Server Example')
    parser.add_argument('--port', action = "store", dest = "port", type = int, required = True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
