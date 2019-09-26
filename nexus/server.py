import socket
import threading
from .client import Client

class Server():

    tn_socket = None
    clients = None

    def __init__(self, port, backlog=10):
        self.tn_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tn_scoket.bind(("", port))
        self.tn_scoket.listen(backlog)

        lock = threading.Lock()
        self.clients = []
        print("Telnet Server Ready")

    def start(self):
        print("Awaiting Connections")
        while True:

            socket, address = self.tn_scoket.accept()
            client = Client(socket, address).start()
            self.clients.append(client)

            print("Connection Established!")
