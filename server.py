#!/usr/bin/python3
import socket
import sys
import clientthread


class Server:

    """Docstring for server.
        This is the server controller.
        It will create a server socket and wait for a client
        then it will hand the client off to a new client tread
        and go back to waiting.
    """

    def __init__(self, sock=None):
        """Initalizes the socket if there is none already. """
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("socket created")

    def bind(self, HOST, PORT):
        """binds the host address and port number to the socket.

        :HOST: local host
        :PORT: 8888

        """
        try:
            self.sock.bind((HOST, PORT))
        except socket.error as msg:
            print("Bind failed. Error code: " +
                  str(msg[0]) + " Message " + msg[1])
            sys.exit
        print("Socket bind complete")

    def main_loop(self):
        """this is where the server waits for a client this takes 10 clients.

        """
        self.sock.listen(10)
        print("socket now listening")
        while True:
            client, addr = self.sock.accept()
            print("Connected with " + addr[0] + ":" + str(addr[1]))
            newthread = clientthread.ClientThread(client, addr, self.port)
            newthread.start()

    def main(self):
        """initializes the host and port binds them and then starts main_loop.


        """
        HOST = ''
        PORT = 8888
        self.port = PORT
        self.host = HOST
        self.bind(self.host, self.port)
        self.main_loop()


def main():
    """creates and starts the server.

    """
    server = Server()
    server.main()


if __name__ == "__main__":
    main()
