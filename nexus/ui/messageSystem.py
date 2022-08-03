import time

class MessageSystem:

    socket = None
    render_speed = None

    def __init__(self, socket, render_speed=0.02):
        self.socket = socket
        self.render_speed = render_speed

    def send(self, message):
        self.socket.send(message.encode())

    def prompt(self):
        self.send("\n\n> ")

    def recieve(self, bufsize=1024):
        return self.socket.recv(bufsize).decode().strip()

    def clear(self):
        self.send("\033c")

    def type(self, message):
        for char in message:
            self.send(char)
            time.sleep(self.render_speed)
