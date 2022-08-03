import os
import re
from enum import Enum
from ..conf import TITLE
from ..dba.databaseManager import DatabaseManager
from .messageSystem import MessageSystem

class NexusArchive:

    address = None
    messageSystem = None
    username = None
    database = None

    def __init__(self, socket, address):
        self.address = address
        self.messageSystem = MessageSystem(socket)

    def __title(self):
        self.messageSystem.send(TITLE)

    def __login(self):
        self.messageSystem.clear()
        self.__title()
        self.messageSystem.send("Username: ")
        self.username = self.messageSystem.recieve()
        
        # Create voyager directory if one does not exist already

    def __select_gate(self):
        gates = {}
        for root, dirs, files in os.walk("archive/gates/"):
            index = 0
            for filename in files:
                if (".sqlite" in filename):
                    index += 1
                    gate = filename.split(".")[0]
                    gate = gate.replace("_", " ")
                    gates[str(index)] = {
                        "title": gate.title(),
                        "file": filename
                    }

        self.messageSystem.clear()
        self.messageSystem.send(TITLE)
        self.messageSystem.send("GATEWAYS:\n")
        for gate_id in gates.keys():
            self.messageSystem.send(f"[{gate_id}] {gates[gate_id]['title']}\n")

        self.messageSystem.send("\nSelect a Gate ID: ")
        gateId = self.messageSystem.recieve()

        if (gateId not in gates.keys()):
            gatefile = self.gateways()
        else:
            gatefile = gates[gateId]["file"]

        self.database = DatabaseManager(gatefile, self.username)

    def __enter_gate(self, entityId=1):

        page = self.database.getLocation(entityId) 
        self.messageSystem.clear()
        self.messageSystem.type(page)

        self.messageSystem.prompt()
        command = self.messageSystem.recieve()
        entityId = self.database.execute(command, entityId)

        if (entityId != 0):
            self.__enter_gate(entityId)

    def start(self):

        try:
            self.__login()
            self.__select_gate()
            self.__enter_gate()

        except Exception as exc:
            print(f"Voyager {self.address} Encountered an Error:\n{exc}")
            self.messageSystem.send("Something Went Wrong!\n")

        finally:
            print(f"Voyager {self.address} Returned Home. Closing Connection")
            self.messageSystem.send("Carry On, Inrepid Voyager!\n")

