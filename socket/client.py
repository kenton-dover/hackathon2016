#!/usr/bin/python3
import socket
import sys


class Client:
    def __init__(self, sock=None):
        """this initializes the socket

        :sock: TODO
        :returns: TODO

        """
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("socket created")

    def connect(self, HOST, PORT):
        """sets up the connection

        :HOST: TODO
        :PORT: TODO
        :returns: TODO

        """
        try:
            self.sock.connect((HOST, PORT))
        except socket.error as msg:
            print("Connect failed. Error Code : " +
                  str(msg[0]) + " Message " + msg[1])
            sys.exit()
        print("Socket connect complete")

    def main_loop(self):
        """this is the main loop fot eh client
        :returns: TODO

        """
        while True:
            data = input()
            self.sock.sendall(str.encode(data))
            data = self.sock.recv(1024)
            data = data.decode("utf-8")
            print(data)
        self.sock.close()

    def main(self):
        """sets up the client
        :returns: TODO

        """
        HOST = '10.1.108.131'
        PORT = 8888
        self.connect(HOST, PORT)
        self.main_loop()


def main():
    """sets up client
    :returns: TODO

    """
    client = Client()
    client.main()


if __name__ == "__main__":
    main()
