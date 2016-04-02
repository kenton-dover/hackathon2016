#!/usr/bin/python3
import threading


class ClientThread(threading.Thread):

    """client Thread that will handle the . """

    def __init__(self, client, addr, port):
        """creates the thread. """
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.port = port

    def run(self):
        """runs the client thread.

        """
        while True:
            data = self.client.recv(1024)
            if not data:
                break
            decoded_data = data.decode("UTF-8")
            print("Client sent: " +
                  decoded_data +
                  " at: " +
                  self.addr[0] +
                  ":" +
                  str(self.addr[1]))
            self.client.send(data)
