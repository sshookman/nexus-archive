class MessageSystem:

    socket = None

    def __init__(self, socket):
        self.socket = socket

    def send(self, message):
        self.socket.send(message.encode())

    def clear(self):
        self.send("\033c")

    def recieve(self, bufsize=1024):
        return self.socket.recv(bufsize).decode()

    def close_socket(self):
        self.socket.close()
