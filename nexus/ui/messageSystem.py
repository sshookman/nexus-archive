import time

class MessageSystem:

    socket = None
    render_speed = None

    def __init__(self, socket, render_speed=0.02):
        self.socket = socket
        self.render_speed = render_speed

    def send(self, message):
        self.socket.send(message.encode())

    def prompt(self, username=None, player=None):
        prefix = "" if (username is None) else f"[{username}]"
        prefix = prefix if (player is None) else prefix += f" {player}"
        self.send(f"\n\n{prefix}> ")

    def password(self, bufsize=1024):
        # TODO: Find a way to tell the client to mask the input
        #self.socket.send(b"\255\254\001")
        pswd = self.recieve(bufsize=bufsize)
        #self.socket.send(b"\255\253\001")
        return pswd

    def recieve(self, bufsize=1024):
        return self.socket.recv(bufsize).decode().strip()

    def clear(self):
        self.send("\033c")

    def type(self, message):
        for char in message:
            self.send(char)
            time.sleep(self.render_speed)
